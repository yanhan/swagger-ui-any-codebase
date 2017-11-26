#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

main() {
	local curdir="$(pwd)"
	docker run \
		--rm \
		--name swagger-demo \
		-v "${curdir}"/server.py:/demo/server.py \
		-v "${curdir}"/api-docs.yml:/demo/api-docs.yml \
		-p 127.0.0.1:5000:5000 \
		swagger-demo
}

main "$@"
# vim:noet
