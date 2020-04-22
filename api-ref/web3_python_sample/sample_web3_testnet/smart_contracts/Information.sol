pragma solidity >=0.4.21 <0.7.0;

contract Information {
    address public owner;

    uint256 public peopleCount = 0;
    mapping(uint256 => UserInformation) public infoList;

    struct UserInformation {
        string name;
        string email;
        string signature;
    }

    UserInformation user;

    constructor() public {
        owner = msg.sender;
    }

    function addInformation(string memory _name, string memory _email,
	string memory _signature) public {
        infoList[peopleCount] = UserInformation(
		 _name, _email, _signature);

    }
}
