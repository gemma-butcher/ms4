// Automatically show the success modal if the form was successfully submitted
document.addEventListener('DOMContentLoaded', function () {
    var successModalElement = document.getElementById('successModal');
    if (successModalElement) {
        var successModal = new bootstrap.Modal(successModalElement);
        successModal.show();
    }
});