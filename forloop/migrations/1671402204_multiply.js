const Multiply = artifacts.require("Multiply")

module.exports = function(_deployer) {
  _deployer.deploy(Multiply)
};
