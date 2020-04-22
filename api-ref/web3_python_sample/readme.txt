1. When developing web3 of python, mostly we use pip instead of anaconda
2. url needs to have http in front to get the correct url 
3. In order to deploy a solidity smart contract => need to compile solidity
    install py-solc using pip
    install solc using python -m solc.install v0.4.25 (currently we must use v0.4.25
    because other versions get this error: https://github.com/ethereum/py-solc/issues/61)
    then copy the directory at $HOME/.py-solc/solc-v0.4.25/bin/solc to 
    /usr/local/bin/. Finally, grant admin permission (chmod -R 777) to the directory
    in the /usr/local/bin/

4. Passing arguments to Solidity functions:
    The data type must be exactly the same. Ex: if in solidity requires byte32 =>
    use bytearray() method to convert string to byte32. Similarly, if it's an 
    array of byte32 => convert all elements into byte32 then pass in

5. VM exception error tends to relate to not passing the require() condition of
    Solidity.

6. Nonce: https://ethereum.stackexchange.com/questions/27432/what-is-nonce-in-ethereum-how-does-it-prevent-double-spending
7. checksum turns all alphabet to uppercase
8. in order to deploy smart contracts onto testnet, we can use Truffle (can use for Python) along with ropsten / rinkeby +
    infaura which is a way to deploy an Ethereum node.
    link for detailed tutorial: https://levelup.gitconnected.com/dapps-development-for-python-developers-f52b32b54f28