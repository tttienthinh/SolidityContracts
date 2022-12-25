// SPDX-License-Identifier: MIT
// compiled with 0.8.17
pragma solidity >=0.4.22 <0.9.0;


contract tmpPair {
  function getReserves() public view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast) {}
}


contract tmpFactory {
  function getReserves() public view returns (uint112 reserve0, uint112 reserve1, uint32 blockTimestampLast) {};
  function allPairs(uint) external view returns (address pair);
  function allPairsLength() external view returns (uint);
}


contract middleMan {
  function getList(address[] memory _add) external view returns (uint[] memory) {
    uint n = _add.length;
    uint[] memory liste = new uint[](n*2);
    
    // Define variables to store the returned values
    uint112 r0;
    uint112 r1;
    uint32 bTLast;
    for (uint i=0; i<n; i++) {
      // Call the getReserves function in the other contract and store the returned values
      (r0, r1, bTLast) = tmpPair(_add[i]).getReserves();
      liste[i*2] = r0;
      liste[i*2+1] = r1;
    }
    
    return liste;
  }



}