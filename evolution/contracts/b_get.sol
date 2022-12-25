// SPDX-License-Identifier: MIT
// compiled with 0.8.17
pragma solidity >=0.4.22 <0.9.0;

contract b {
    
    function getFavoriteNumber() public view returns(uint) {}
    
    function setFavoriteNumber(uint _favoriteNumber) public {}
    
}

contract b_get {

    function getA(address _t) public view returns (uint result) {
        return b(_t).getFavoriteNumber();
    }
    
    function setA(address _t, uint _val) public {
        b(_t).setFavoriteNumber(_val);
    }
}
