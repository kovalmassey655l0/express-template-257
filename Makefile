.PHONY: build test clean run

build:
	@echo "Building express-template-257..."
	go build -o bin/express-template-257 ./cmd/...

test:
	go test ./... -v -cover

clean:
	rm -rf bin/ dist/

run: build
	./bin/express-template-257
