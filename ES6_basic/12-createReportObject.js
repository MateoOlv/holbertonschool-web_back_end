export default function createReportObject(employeesList) {
  const ReportObject = {
    allEmployees: employeesList,
    getNumberOfDepartments(employeesList) {
      return Object.keys(employeesList).length; },
  };
  return ReportObject;
}