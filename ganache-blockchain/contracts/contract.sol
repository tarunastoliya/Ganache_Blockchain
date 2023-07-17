// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract HelloWorld {
   
    string [] public payload;
    //mapping (string => uint) public Payload;
    function setPayload(string memory content) public {
      //  Payload[content] = 1;
        payload.push(content);
    }
    function sayHello(string memory _stringTest) view public returns (string memory) {
        //return (Payload[_stringTest] ==  1)? "Valid Entry" : "Invalid";
        uint arrayLength = payload.length;
        for(int i = 0;i < int(arrayLength);i++){
            if (keccak256(abi.encodePacked(payload[uint(i)])) == keccak256(abi.encodePacked(_stringTest))){
                return "Valid Entry";
            }
        }
        return "Invalid Entry";
    }
}
