export default function createEmployeesObject(departmentName, employees) {
  const depEmployees = {
    [`${departmentName}`]: [...employees],
  };
  return depEmployees;
}