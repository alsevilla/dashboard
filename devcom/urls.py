from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'index'),
    #data input
    #facebook
    path('data_input_fb_page_info', views.data_input_fb_page_info, name='data_input_fb_page_info'),
    path('fb_page_infos', views.fb_page_infos, name='fb_page_infos'),
    path('fb_page_infos_edit/<str:pk>', views.fb_page_infos_edit, name='fb_page_infos_edit'),
    path('fb_page_infos_delete/<str:pk>', views.fb_page_infos_delete, name='fb_page_infos_delete'),
    path('facebook_page_info', views.facebook_page_info, name='facebook_page_info'),
    path('data_input_fb_post_data', views.data_input_fb_post_data, name='data_input_fb_post_data'),
    path('fb_post_data', views.fb_posts_data, name='fb_post_data'),
    path('fb_post_data_edit/<str:pk>',views.fb_posts_data_edit, name='fb_post_data_edit'),
    path('fb_post_data_delete/<str:pk>',views.fb_posts_data_delete, name='fb_post_data_delete'),
    path('facebook_post_data', views.facebook_post_data, name='facebook_post_data'),

    #end facebook
    #ptc
    path('data_input_ptc', views.data_input_ptc, name='data_input_ptc'),
    path('ptc',views.ptcs, name='ptc'),
    path('ptc_edit/<str:pk>', views.ptcs_edit, name='ptc_edit'),
    path('ptc_delete/<str:pk>',views.ptcs_delete, name='ptc_delete'),
    path('ptc_table', views.philricetextcenter, name='ptc_table'),
    #end ptc
    path('data_input_pw', views.data_input_pw, name='data_input_pw'),#PhilRice website
    path('pw', views.pws, name='pw'),
    path('pw_edit/<str:pk>', views.pws_edit, name='pw_edit'),
    path('pw_delete/<str:pk>',views.pws_delete, name='pw_delete'),
    path('data_input_pw_visitor', views.data_input_pw_visitor, name='data_input_pw_visitor'),#PhilRice website
    path('pw_visitor', views.pws_visitor, name='pw_visitor'),
    path('pw_visitor_edit/<str:pk>', views.pws_visitor_edit, name='pw_visitor_edit'),
    path('pw_visitor_delete/<str:pk>', views.pws_visitor_delete, name='pw_visitor_delete'),
    #Pinoy Rice
    path('data_input_pr_visitor', views.data_input_pr_visitor, name='data_input_pr_visitor'),
    path('pr_visitor', views.prs_visitor, name='pr_visitor'),
    path('pr_visitor_edit/<str:pk>', views.prs_visitor_edit, name='pr_visitor_edit'),
    path('pr_visitor_delete/<str:pk>', views.prs_visitor_delete, name='pr_visitor_delete'),
    path('data_input_pr_upload', views.data_input_pr_upload, name='data_input_pr_upload'),
    path('pr_upload', views.prs_upload, name='pr_upload'),
    path('pr_upload_edit/<str:pk>', views.prs_upload_edit, name='pr_upload_edit'),
    path('pr_upload_delete/<str:pk>', views.prs_upload_delete, name='pr_upload_delete'),
    path('pr_table', views.pinoyrice_visitor, name='pr_table'),
    path('pr_upload_table', views.pinoyrice_upload, name='pr_upload_table'),
    #end Pinoy Rice
    #radio
    path('data_input_radio_visitor', views.data_input_radio_visitor, name='data_input_radio_visitor'),
    path('radio_visitor', views.radios_visitor, name='radio_visitor'),
    path('radio_visitor_edit/<str:pk>',views.radios_visitor_edit, name='radio_visitor_edit'),
    path('radio_visitor_delete/<str:pk>', views.radios_visitor_delete, name='radio_visitor_delete'),
    path('data_input_radio_upload', views.data_input_radio_upload, name='data_input_radio_upload'),
    path('radio_upload', views.radios_upload, name='radio_upload'),
    path('radio_upload_edit/<str:pk>',views.radios_upload_edit, name='radio_upload_edit'),
    path('radio_upload_delete/<str:pk>', views.radios_upload_delete, name='radio_upload_delete'),
    #end radio
    # kp
    path('data_input_kp', views.data_input_kp, name='data_input_kp'),
    path('kp_edit/<str:pk>', views.kps_edit, name='kp_edit'),
    path('kp_delete/<str:pk>', views.kps_delete, name='kp_delete'),
    path('data_input_kp_stock', views.data_input_kp_stock, name='data_input_kp_stock'),
    path('kp_stocks_transactions/<str:pk>', views.kp_stock_transaction, name='kp_stocks_transactions'),
    path('kp_edit_stock/<str:pk>', views.kps_edit_stock, name='kp_edit_stock'),
    path('kp_delete_stock/<str:pk>', views.kps_delete_stock, name='kp_delete_stock'),
    path('data_input_kp_recipient', views.data_input_kp_recipient, name='data_input_kp_recipient'),
    path('kp_recipient_edit/<str:pk>', views.kp_recipient_edit, name='kp_recipient_edit'),
    path('kp_recipient_delete/<str:pk>', views.kp_recipient_delete, name='kp_recipient_delete'),
    path('data_input_kp_distribute/<str:pk>', views.kp_distribution, name='data_input_kp_distribute'),
    path('data_input_kp_distribute_delete/<str:pk>', views.kp_distribution_delete, name='data_input_kp_distribute_delete'),
    path('kp_stock_view', views.kp_stock_view, name='kp_stock_view'),
    path('kp_tables', views.kp_table, name='kp_tables'),
    # end kp
    path('data_input_partners', views.data_input_partners, name='data_input_partners'),
    path('partners', views.partner_data, name='partners'),
    path('partners_edit/<str:pk>', views.partner_edit, name='partners_edit'),
    path('partners_delete/<str:pk>', views.partner_delete, name='partners_delete'),
    path('data_input_intermediaries', views.data_input_intermediaries, name='data_input_intermediaries'),
    #DevCom
    path('data_input_progproj', views.data_input_progproj, name='data_input_progproj'),
    path('data_input_publication', views.data_input_publication, name='data_input_publication'),
    path('data_input_awards', views.data_input_awards, name='data_input_awards'),
    path('data_input_staff', views.data_input_staff, name='data_input_staff'),
    #end Devcom
    #end of datainput

    path('pw_table', views.philricewebsite, name='pw_table'),
    path('pw_visitor_table', views.philricewebsite_visitor, name='pw_visitor_table'),



    path('radio', views.radio, name='radio'),

    path('partner', views.partner, name='partner'),

    path('progproj', views.programprojects, name='progproj'),
    path('progproj_edit/<str:pk>', views.programprojects_edit, name='progproj_edit'),
    path('progproj_delete/<str:pk>', views.programprojects_delete, name='progproj_delete'),

    path('publications', views.publications, name='publications'),
    path('publications_edit/<str:pk>', views.publications_edit, name='publications_edit'),
    path('publications_delete/<str:pk>', views.publications_delete, name='publications_delete'),

    path('awards', views.award, name='awards'),
    path('awards_edit/<str:pk>', views.award_edit, name='awards_edit'),
    path('awards_delete/<str:pk>', views.award_delete, name='awards_delete'),

    path('staffs', views.staffs, name='staffs'),
    path('staffs_edit/<str:pk>', views.staffs_edit, name='staffs_edit'),
    path('staffs_delete/<str:pk>', views.staffs_delete, name='staffs_delete'),
]
