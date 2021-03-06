SHELL = /bin/bash

SERVICES = \
	microservices/api/gateway \
	microservices/svc/greeter \
	microservices/svc/adder \
	microservices/svc/subtractor \
	microservices/svc/multiplier \
	microservices/svc/divider \

.PHONY: all
all: proto pre fmt lint

.PHONY: install
install:
	make -C .devcontainer install


.PHONY: pre
pre:
	@for f in $(SERVICES); do make -C $$f pre; done

.PHONY: fmt
fmt:
	@for f in $(SERVICES); do make -C $$f fmt; done

.PHONY: lint
lint:
	@for f in $(SERVICES); do make -C $$f lint; done


.PHONY: proto
proto:
	buf mod update
	buf generate


.PHONY: build
build:
	skaffold build


.PHONY: kind
kind:
	kind get clusters -q | grep "distributed-calculator" || kind create cluster --config kind.yaml

.PHONY: clean
clean:
	kind delete cluster --name distributed-calculator

.PHONY: dev
dev:
	skaffold dev


.PHONY: deploy-production
deploy-production:
	docker login registry-intern2021.jp-east-1.gitlab.devops.nifcloud.com
	kubectl create secret generic regcred --from-file=.dockerconfigjson=$(HOME)/.docker/config.json --type=kubernetes.io/dockerconfigjson || true
	skaffold run -p production

.PHONY: destroy-production
destroy-production:
	kubectl delete secret regcred
	skaffold delete -p production


.PHONY: http
http:
	curl -i localhost:58080/greeter/hello -H "Content-Type: application/json" -d '{"name": "alice"}'

.PHONY: grpc
grpc:
	grpcurl -protoset <(buf build -o -) -plaintext -d '{"name": "alice"}' localhost:55050 distributed-calculator.greeter.v1.Greeter/Hello || true
