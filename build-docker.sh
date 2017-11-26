#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

main() {
	docker build -t swagger-demo .
}

main "$@"
# vim:noet
