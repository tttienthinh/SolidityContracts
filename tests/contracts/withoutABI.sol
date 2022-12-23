// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract withoutABI {
  function callOtherContract(address otherContract) public view returns (uint) {
    // Call the function "doSomething" on the other contract
    // with no arguments and no return value
    (bool success, bytes memory data) = otherContract.call(bytes4(keccak256("getFavoriteNumber()")));

    require(success, "Call failed");
    uint256 result;
    assembly {
      result := mload(add(data, 0x20))
    }
    return result;
  }
}
