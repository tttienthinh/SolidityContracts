const b_get = artifacts.require("b_get")

module.exports = function(_deployer) {
  _deployer.deploy(b_get)
};