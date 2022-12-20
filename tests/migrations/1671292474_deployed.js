const Deployed = artifacts.require("Deployed")

module.exports = function(_deployer) {
	_deployer.deploy(Deployed);
};
