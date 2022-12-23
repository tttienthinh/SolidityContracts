// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract UniswapTrue {
      uint112 public r0;           // uses single storage slot, accessible via getReserves
    uint112 public r1;           // uses single storage slot, accessible via getReserves
    uint32  public bTL; // uses single storage slot, accessible via getReserves
  
  constructor() public {
    r0 = 2;
    r1 = 3;
    bTL = 4;
  }

    function getReserves() public view returns (uint112 _reserve0, uint112 _reserve1, uint32 _blockTimestampLast) {
        _reserve0 = r0;
        _reserve1 = r1;
        _blockTimestampLast = bTL;
    }
}
