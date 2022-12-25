const getReserve = artifacts.require("middleMan")

module.exports = function(_deployer) {
  _deployer.deploy(getReserve)
};
