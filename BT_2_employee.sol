// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract EmployeeDetails {
    // Structure to store employee information
    struct Employee {
        uint256 id;
        string name;
        uint256 salary;
        string joiningDate;
    }

    // Mapping to store employee details using ID
    mapping(uint256 => Employee) private employees;
    uint256 public employeeCount;

    // Event to log when employee is added
    event EmployeeAdded(uint256 id, string name, uint256 salary, string joiningDate);

    // Function to add a new employee
    function addEmployee(uint256 _id, string memory _name, uint256 _salary, string memory _joiningDate) public {
        employees[_id] = Employee(_id, _name, _salary, _joiningDate);
        employeeCount++;
        emit EmployeeAdded(_id, _name, _salary, _joiningDate);
    }

    // Function to view an employee by ID
    function getEmployee(uint256 _id) public view returns (uint256, string memory, uint256, string memory) {
        Employee memory e = employees[_id];
        require(e.id != 0, "Employee not found");
        return (e.id, e.name, e.salary, e.joiningDate);
    }

    // Function to get total employees added
    function getTotalEmployees() public view returns (uint256) {
        return employeeCount;
    }
}
