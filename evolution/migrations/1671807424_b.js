const b = artifacts.require("b")

module.exports = function(_deployer) {
  _deployer.deploy(b)
};