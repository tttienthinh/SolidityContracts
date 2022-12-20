const Deployed = artifacts.require("./Deployed");
const Existing = artifacts.require("./Existing");
let address = '0x678945d819cCe23b83b9e3ab5b1958Aa123Efe5D';


contract("Deployed", accounts => {
    it("Get address account", async function() {
        const Contract = await Deployed.deployed();
        const result = await Contract.a({from: accounts[0]});
        address = Contract.contract._address;
        console.log(address);
    })
    it("Set", async function() {
        const Contract = await Deployed.deployed();
        const result = await Contract.setA(47, {from: accounts[0]});
    })
    it("Get", async function() {
        const Contract = await Deployed.deployed();
        const result = await Contract.a({from: accounts[0]});
        console.log(result);
    })
})

contract("Existing", accounts => {
    it("Set address account", async function() {
        const Contract = await Existing.deployed();
        const result = await Contract.existing(address, {from: accounts[0]});
        console.log(address);
    })
    it("Get", async function() {
        const Contract = await Existing.deployed();
        const result = await Contract.getA({from: accounts[0]});
        console.log(result);
    })
    it("Set", async function() {
        const Contract = await Existing.deployed();
        const result = await Contract.setA(42, {from: accounts[0]});
        console.log(address);
    })
    it("Get", async function() {
        const Contract = await Existing.deployed();
        const result = await Contract.getA({from: accounts[0]});
        console.log(result);
    })

})
