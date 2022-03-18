const readline = require('readline');

const rl = readline.createInterface({
	input : process.stdin,
	output : process.stdout,
});

let str = '';
let check = 0;

rl.on("line", function(line) {
	if (check == 1)
		str += '\n';
	str += line;
	check = 1;
}).on("close", function() {
	console.log(str);
	process.exit();
})