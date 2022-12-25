const a = artifacts.require("a")

module.exports = function(_deployer) {
  _deployer.deploy(a)
};