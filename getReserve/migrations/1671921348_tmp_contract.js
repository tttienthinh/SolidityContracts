const tmpContract = artifacts.require("tmpContract")

module.exports = function(_deployer) {
  _deployer.deploy(tmpContract)
};
