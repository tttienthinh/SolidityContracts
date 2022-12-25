// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract a {
    function getFavoriteNumber() public view returns(uint) {}
    function getFavoriteNumber2() public pure returns(uint) {}
}

contract a_get {
    function getA(address _t) public view returns (uint) {
        return a(_t).getFavoriteNumber();
    }
    function getA2(address _t) public pure returns (uint) {
        return a(_t).getFavoriteNumber2();
    }
}