function validatesal() {
    let sal = document.getElementById('id_salary').value;

    if (sal < 0) {
        window.alert('salary should not be negative');
    }


}