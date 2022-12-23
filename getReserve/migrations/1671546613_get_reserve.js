const getReserve = artifacts.require("getReserve")

module.exports = function(_deployer) {
  _deployer.deploy(getReserve)
};
