// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract Multiply {
    function sommeN(uint256 n) external pure returns (uint256) {
        uint256 somme = 0;

        for (uint256 i = 0; i <= n; i++) {
            somme = somme + i;
        }
        return somme;
    }

    function sommeA(uint256[] memory _arr) external pure returns (uint256) {
        uint n = _arr.length;
        uint somme = 0;
        for (uint i=0; i<n; i++) {
          somme = somme + _arr[i];
        }
        return somme;
    }
}
