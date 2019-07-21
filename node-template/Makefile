default: trans; cargo build

trans:
	python3 ./gen_cargo.py
	mv Cargo.toml Cargo.toml.bak
	mv deps.toml Cargo.toml
	cd runtime; make trans
trans-back:
	mv Cargo.toml.bak Cargo.toml

replace:
	grep -rl node-template -R ./ | xargs -r sed -i "s/node-template/$(name)/g"
	grep -rl node_template -R ./ | xargs -r sed -i "s/node_template/$(name)/g"
