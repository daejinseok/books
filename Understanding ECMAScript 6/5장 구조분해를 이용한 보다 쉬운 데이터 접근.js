

let node = {
    type: "Identifiter",
    name: "foo"
};

let { type, name } = node;

console.log(type);
console.log(name);

// > node "5장 구조분해를 이용한 보다 쉬운 데이터 접근.js"
// Identifiter
// foo


let node = {
    type: "Identifier",
    name: "foo"
},
type = "Literal";
name = 5;

({type, name} = node);

// 구조분해 할당문은 괄호로 감싸야 한다!!
//
// 여는 중괄호가 불록문의 시작을 의미하며,
// 블록문은 할당문 왼쪽에 위치할 수 없음.
// 괄호는 다음에 오는 중괄호가 블록문이 아님을 알리고,
// 표현식으로 해석되어 할당이 완료되도록 한다.



console.log(type);
console.log(name);



let node = {
    type: "Id"
}