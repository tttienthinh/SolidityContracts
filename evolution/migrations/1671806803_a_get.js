const a_get = artifacts.require("a_get")

module.exports = function(_deployer) {
  _deployer.deploy(a_get)
};