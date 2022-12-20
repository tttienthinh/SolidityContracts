// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract Deployed {    
    uint public a = 1;
    
    function setA(uint _a) public returns (uint) {
        a = _a;
        return a;
    }
    
}