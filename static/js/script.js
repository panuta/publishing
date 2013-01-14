
function _switch_signup_login_modal(tab_name) {
    var modal = $('#modal-signup-login');
    modal.find('.nav-tabs li').removeClass('active');
    modal.find('.tab-content .tab-pane').removeClass('active');

    if(tab_name == 'signup') {
        modal.find('.nav-tabs a[href="#modal-tab-signup"]').parent().addClass('active');
        $('#modal-tab-signup').addClass('active');
    } else if(tab_name == 'login') {
        modal.find('.nav-tabs a[href="#modal-tab-login"]').parent().addClass('active');
        $('#modal-tab-login').addClass('active');
    }
}
