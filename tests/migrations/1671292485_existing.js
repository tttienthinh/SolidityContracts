const Existing = artifacts.require("Existing")

module.exports = function(_deployer) {
  _deployer.deploy(Existing);
};
