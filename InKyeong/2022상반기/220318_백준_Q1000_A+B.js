// readline 모듈을 import
const readline = require('readline');

// 인터페이스 객체 생성
// process의 입출력 스트림을 input과 output에 할당
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.on('line', function (line) {
    const input = line.split(' ');

    const result = Number(input[0]) + Number(input[1]);
    console.log(result);

    rl.close();
}).on('close', function () {
    process.exit();
});