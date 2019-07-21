default: trans; cargo build

trans:
	python3 ./scripts/gen_cargo.py
	Cd runtime; python3 ./scripts/gen_cargo.py

replace:
	grep -rl node-template -R ./ | xargs -r sed -i "s/node-template/$(name)/g"
	grep -rl node_template -R ./ | xargs -r sed -i "s/node_template/$(name)/g"
