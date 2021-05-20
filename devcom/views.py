from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.db.models.functions import Concat
from django.db.models import Value, Sum
import django.utils.timezone as timezone
from django.db import connections

def dashboard(request):
    dashboard = 'active'
    cur_year = timezone.now().year
    prev_year = cur_year - 1
    awards_count = awards.objects.count()
    publications_count = publication.objects.count()
    projects_count = progproj.objects.filter(status='Active').count()
    staff_count = staff.objects.filter(status='active').count()
    ongoing_project = progproj.objects.filter(status='Active')
    staff_active = staff.objects.filter(status='active')

    for fb_page_data1 in fb_page_info.objects.raw(""" SELECT id, IFNULL(SUM(likes),0) as likes, IFNULL(SUM(followers),0) as followers, IFNULL(SUM(allpost),0) as allpost FROM fb_page_info WHERE year=%s""",[cur_year]):
        like_cur_count = fb_page_data1.likes
        follow_cur_count = fb_page_data1.followers
        allpost_cur_count = fb_page_data1.allpost
    for fb_page_data2 in fb_page_info.objects.raw(""" SELECT id, IFNULL(SUM(likes),0) as likes, IFNULL(SUM(followers),0) as followers, IFNULL(SUM(allpost),0) as allpost FROM fb_page_info WHERE year=%s""",[prev_year]):
        like_prev_count = fb_page_data2.likes
        follow_prev_count = fb_page_data2.followers
        allpost_prev_count = fb_page_data2.allpost
    for fb_post_data1 in fb_post_data.objects.raw(""" SELECT id, IFNULL(SUM(messagesRecieve),0) as messagesRecieve, IFNULL(SUM(responseRate),0) as responseRate, IFNULL(SUM(nSurvey),0) as nSurvey FROM fb_post_data WHERE year=%s """,[cur_year]):
        messagesRecieve_cur_count = fb_post_data1.messagesRecieve
        responseRate_cur_count = fb_post_data1.responseRate
        nSurvey_cur_count = fb_post_data1.nSurvey
    for fb_post_data1 in fb_post_data.objects.raw(""" SELECT id, IFNULL(SUM(messagesRecieve),0) as messagesRecieve, IFNULL(SUM(responseRate),0) as responseRate, IFNULL(SUM(nSurvey),0) as nSurvey FROM fb_post_data WHERE year=%s """,[prev_year]):
        messagesRecieve_prev_count = fb_post_data1.messagesRecieve
        responseRate_prev_count = fb_post_data1.responseRate
        nSurvey_prev_count = fb_post_data1.nSurvey

    for ptc_registered_data1 in ptc.objects.raw(""" SELECT id, IFNULL(SUM(total), 0) as total, year FROM(SELECT id, SUM(abra) as total, year from ptc GROUP BY year UNION ALL SELECT id, SUM(agusanNorte) as total, year from ptc GROUP BY year UNION ALL SELECT id, SUM(agusanSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(aklan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(albay), year from ptc GROUP BY year UNION ALL SELECT id, SUM(antique), year from ptc GROUP BY year UNION ALL SELECT id, SUM(apayao), year from ptc GROUP BY year UNION ALL SELECT id, SUM(aurora), year from ptc GROUP BY year UNION ALL SELECT id, SUM(basilan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(bataan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(batanes), year from ptc GROUP BY year UNION ALL SELECT id, SUM(benguet), year from ptc GROUP BY year UNION ALL SELECT id, SUM(biliran), year from ptc GROUP BY year UNION ALL SELECT id, SUM(bohol), year from ptc GROUP BY year UNION ALL SELECT id, SUM(bukidnon), year from ptc GROUP BY year UNION ALL SELECT id, SUM(bulacan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(cagayan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(camarinesNorte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(camarinesSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(camiguin), year from ptc GROUP BY year UNION ALL SELECT id, SUM(capiz), year from ptc GROUP BY year UNION ALL SELECT id, SUM(catanduanes), year from ptc GROUP BY year UNION ALL SELECT id, SUM(cavite), year from ptc GROUP BY year UNION ALL SELECT id, SUM(cebu), year from ptc GROUP BY year UNION ALL SELECT id, SUM(compostela), year from ptc GROUP BY year UNION ALL SELECT id, SUM(davaoNorte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(davaoSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(davaoOriental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(samarEast), year from ptc GROUP BY year UNION ALL SELECT id, SUM(guimaras), year from ptc GROUP BY year UNION ALL SELECT id, SUM(ifugao), year from ptc GROUP BY year UNION ALL SELECT id, SUM(ilocosNorte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(ilocosSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(iloilo), year from ptc GROUP BY year UNION ALL SELECT id, SUM(isabela), year from ptc GROUP BY year UNION ALL SELECT id, SUM(kalinga), year from ptc GROUP BY year UNION ALL SELECT id, SUM(launion), year from ptc GROUP BY year UNION ALL SELECT id, SUM(lanaoNorte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(lanaoSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(leyte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(maguindanao), year from ptc GROUP BY year UNION ALL SELECT id, SUM(marinduque), year from ptc GROUP BY year UNION ALL SELECT id, SUM(masbate), year from ptc GROUP BY year UNION ALL SELECT id, SUM(manila), year from ptc GROUP BY year UNION ALL SELECT id, SUM(misamisOccidental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(misamisOriental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(mountainProvince), year from ptc GROUP BY year UNION ALL SELECT id, SUM(negrosOccidental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(negrosOriental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(cotabatoNorth), year from ptc GROUP BY year UNION ALL SELECT id, SUM(samarNorth), year from ptc GROUP BY year UNION ALL SELECT id, SUM(nuevaEcija), year from ptc GROUP BY year UNION ALL SELECT id, SUM(nuevaVizcaya), year from ptc GROUP BY year UNION ALL SELECT id, SUM(mindoroOccidental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(mindoroOriental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(palawan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(pangasinan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(quezon), year from ptc GROUP BY year UNION ALL SELECT id, SUM(quirino), year from ptc GROUP BY year UNION ALL SELECT id, SUM(rizal), year from ptc GROUP BY year UNION ALL SELECT id, SUM(romblon), year from ptc GROUP BY year UNION ALL SELECT id, SUM(samar), year from ptc GROUP BY year UNION ALL SELECT id, SUM(sarangani), year from ptc GROUP BY year UNION ALL SELECT id, SUM(siquijor), year from ptc GROUP BY year UNION ALL SELECT id, SUM(sorsogon), year from ptc GROUP BY year UNION ALL SELECT id, SUM(cotabatoSouth), year from ptc GROUP BY year UNION ALL SELECT id, SUM(leyteSouth), year from ptc GROUP BY year UNION ALL SELECT id, SUM(sultanKudarat), year from ptc GROUP BY year UNION ALL SELECT id, SUM(sulu), year from ptc GROUP BY year UNION ALL SELECT id, SUM(surigaoNorte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(surigaoSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(tarlac), year from ptc GROUP BY year UNION ALL SELECT id, SUM(tawitawi), year from ptc GROUP BY year UNION ALL SELECT id, SUM(zambales), year from ptc GROUP BY year UNION ALL SELECT id, SUM(zamboangaNorte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(zamboangaSibugay), year from ptc GROUP BY year UNION ALL SELECT id, SUM(zamboangaSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(international), year from ptc GROUP BY year UNION ALL SELECT id, SUM(undetermined), year from ptc GROUP BY year) as ha WHERE year=%s """,[cur_year]):
        registered_cur_count = ptc_registered_data1.total

    for ptc_registered_data2 in ptc.objects.raw(""" SELECT id, IFNULL(SUM(total), 0) as total, year FROM(SELECT id, SUM(abra) as total, year from ptc GROUP BY year UNION ALL SELECT id, SUM(agusanNorte) as total, year from ptc GROUP BY year UNION ALL SELECT id, SUM(agusanSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(aklan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(albay), year from ptc GROUP BY year UNION ALL SELECT id, SUM(antique), year from ptc GROUP BY year UNION ALL SELECT id, SUM(apayao), year from ptc GROUP BY year UNION ALL SELECT id, SUM(aurora), year from ptc GROUP BY year UNION ALL SELECT id, SUM(basilan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(bataan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(batanes), year from ptc GROUP BY year UNION ALL SELECT id, SUM(benguet), year from ptc GROUP BY year UNION ALL SELECT id, SUM(biliran), year from ptc GROUP BY year UNION ALL SELECT id, SUM(bohol), year from ptc GROUP BY year UNION ALL SELECT id, SUM(bukidnon), year from ptc GROUP BY year UNION ALL SELECT id, SUM(bulacan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(cagayan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(camarinesNorte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(camarinesSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(camiguin), year from ptc GROUP BY year UNION ALL SELECT id, SUM(capiz), year from ptc GROUP BY year UNION ALL SELECT id, SUM(catanduanes), year from ptc GROUP BY year UNION ALL SELECT id, SUM(cavite), year from ptc GROUP BY year UNION ALL SELECT id, SUM(cebu), year from ptc GROUP BY year UNION ALL SELECT id, SUM(compostela), year from ptc GROUP BY year UNION ALL SELECT id, SUM(davaoNorte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(davaoSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(davaoOriental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(samarEast), year from ptc GROUP BY year UNION ALL SELECT id, SUM(guimaras), year from ptc GROUP BY year UNION ALL SELECT id, SUM(ifugao), year from ptc GROUP BY year UNION ALL SELECT id, SUM(ilocosNorte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(ilocosSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(iloilo), year from ptc GROUP BY year UNION ALL SELECT id, SUM(isabela), year from ptc GROUP BY year UNION ALL SELECT id, SUM(kalinga), year from ptc GROUP BY year UNION ALL SELECT id, SUM(launion), year from ptc GROUP BY year UNION ALL SELECT id, SUM(lanaoNorte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(lanaoSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(leyte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(maguindanao), year from ptc GROUP BY year UNION ALL SELECT id, SUM(marinduque), year from ptc GROUP BY year UNION ALL SELECT id, SUM(masbate), year from ptc GROUP BY year UNION ALL SELECT id, SUM(manila), year from ptc GROUP BY year UNION ALL SELECT id, SUM(misamisOccidental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(misamisOriental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(mountainProvince), year from ptc GROUP BY year UNION ALL SELECT id, SUM(negrosOccidental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(negrosOriental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(cotabatoNorth), year from ptc GROUP BY year UNION ALL SELECT id, SUM(samarNorth), year from ptc GROUP BY year UNION ALL SELECT id, SUM(nuevaEcija), year from ptc GROUP BY year UNION ALL SELECT id, SUM(nuevaVizcaya), year from ptc GROUP BY year UNION ALL SELECT id, SUM(mindoroOccidental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(mindoroOriental), year from ptc GROUP BY year UNION ALL SELECT id, SUM(palawan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(pangasinan), year from ptc GROUP BY year UNION ALL SELECT id, SUM(quezon), year from ptc GROUP BY year UNION ALL SELECT id, SUM(quirino), year from ptc GROUP BY year UNION ALL SELECT id, SUM(rizal), year from ptc GROUP BY year UNION ALL SELECT id, SUM(romblon), year from ptc GROUP BY year UNION ALL SELECT id, SUM(samar), year from ptc GROUP BY year UNION ALL SELECT id, SUM(sarangani), year from ptc GROUP BY year UNION ALL SELECT id, SUM(siquijor), year from ptc GROUP BY year UNION ALL SELECT id, SUM(sorsogon), year from ptc GROUP BY year UNION ALL SELECT id, SUM(cotabatoSouth), year from ptc GROUP BY year UNION ALL SELECT id, SUM(leyteSouth), year from ptc GROUP BY year UNION ALL SELECT id, SUM(sultanKudarat), year from ptc GROUP BY year UNION ALL SELECT id, SUM(sulu), year from ptc GROUP BY year UNION ALL SELECT id, SUM(surigaoNorte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(surigaoSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(tarlac), year from ptc GROUP BY year UNION ALL SELECT id, SUM(tawitawi), year from ptc GROUP BY year UNION ALL SELECT id, SUM(zambales), year from ptc GROUP BY year UNION ALL SELECT id, SUM(zamboangaNorte), year from ptc GROUP BY year UNION ALL SELECT id, SUM(zamboangaSibugay), year from ptc GROUP BY year UNION ALL SELECT id, SUM(zamboangaSur), year from ptc GROUP BY year UNION ALL SELECT id, SUM(international), year from ptc GROUP BY year UNION ALL SELECT id, SUM(undetermined), year from ptc GROUP BY year) as ha WHERE year=%s """,[prev_year]):
        registered_prev_count = ptc_registered_data2.total

    for ptc_data1 in ptc.objects.raw(""" SELECT id, year, IFNULL(SUM(sms), 0) as sms, IFNULL(SUM(smsWD)/12, 0) as smsWD FROM ptc WHERE year=%s """,[cur_year]):
        sms_cur_count = ptc_data1.sms
        smsWD_cur_count = ptc_data1.smsWD

    for ptc_data2 in ptc.objects.raw(""" SELECT id, year, IFNULL(SUM(sms), 0) as sms, IFNULL(SUM(smsWD)/12, 0) as smsWD FROM ptc WHERE year=%s """,[prev_year]):
        sms_prev_count = ptc_data2.sms
        smsWD_prev_count = ptc_data2.smsWD

    for ptc_response1 in ptc.objects.raw(""" SELECT id, IFNULL(SUM(total),0) as total, year FROM (
    SELECT id, IFNULL(SUM(OH1to5), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH6to10), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH11to15), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH16to20), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH21to25), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH26to30), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH31to1h), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH1hto2h), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH2hto4h), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH4hto8h), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH8hto12h), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH12hto24h), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH24to48h), 0) as total, year FROM ptc GROUP BY year
    ) as t WHERE year=%s""",[cur_year]):
        responseptc_cur_count = ptc_response1.total

    for ptc_response2 in ptc.objects.raw(""" SELECT id, IFNULL(SUM(total),0) as total, year FROM (
    SELECT id, IFNULL(SUM(OH1to5), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH6to10), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH11to15), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH16to20), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH21to25), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH26to30), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH31to1h), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH1hto2h), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH2hto4h), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH4hto8h), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH8hto12h), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH12hto24h), 0) as total, year FROM ptc GROUP BY year UNION ALL
    SELECT id, IFNULL(SUM(OH24to48h), 0) as total, year FROM ptc GROUP BY year
    ) as t WHERE year=%s""",[prev_year]):
        responseptc_prev_count = ptc_response2.total

    for pw_data1 in pw_visitor.objects.raw('SELECT id, IFNULL(SUM(visit),0) AS visit, IFNULL(SUM(pageviews),0) AS pageviews FROM pw_visitor WHERE year=%s',[cur_year]):
        pw_visit_cur_count = pw_data1.visit
        pw_pageviews_cur_count = pw_data1.pageviews

    for pw_data2 in pw_visitor.objects.raw('SELECT id, IFNULL(SUM(visit),0) AS visit, IFNULL(SUM(pageviews),0) AS pageviews FROM pw_visitor WHERE year=%s',[prev_year]):
        pw_visit_prev_count = pw_data2.visit
        pw_pageviews_prev_count = pw_data2.pageviews

    for pw_data3 in pw.objects.raw('SELECT id, IFNULL(COUNT(title),0) as stories, year FROM pw WHERE year=%s',[cur_year]):
        pw_stories_cur_count = pw_data3.stories

    for pw_data4 in pw.objects.raw('SELECT id, IFNULL(COUNT(title),0) as stories, year FROM pw WHERE year=%s',[prev_year]):
        pw_stories_prev_count = pw_data4.stories

    for prkb_data1 in pr_visitor.objects.raw('SELECT id, IFNULL(SUM(visit),0) as visit, IFNULL(SUM(download),0) as download, IFNULL(SUM(pageviews),0) as pageviews FROM pr_visitor WHERE year=%s',[cur_year]):
        visit_cur_count = prkb_data1.visit
        download_cur_count = prkb_data1.download
        pageviews_cur_count = prkb_data1.pageviews

    for prkb_data2 in pr_visitor.objects.raw('SELECT id, IFNULL(SUM(visit),0) as visit, IFNULL(SUM(download),0) as download, IFNULL(SUM(pageviews),0) as pageviews FROM pr_visitor WHERE year=%s',[prev_year]):
        visit_prev_count = prkb_data2.visit
        download_prev_count = prkb_data2.download
        pageviews_prev_count = prkb_data2.pageviews

    for prkb_data3 in pr_upload.objects.raw('SELECT id, COUNT(title) as title FROM pr_upload WHERE year=%s',[cur_year]):
        upload_cur_count = prkb_data3.title

    for prkb_data4 in pr_upload.objects.raw('SELECT id, COUNT(title) as title FROM pr_upload WHERE year=%s',[prev_year]):
        upload_prev_count = prkb_data4.title

    for distribute_data1 in kp_distribute.objects.raw('SELECT id, IFNULL(SUM(Quantity),0) as total FROM `kp_distribute` WHERE Year=%s',[cur_year]):
        distribute_cur_count = distribute_data1.total

    for distribute_data2 in kp_distribute.objects.raw('SELECT id, IFNULL(SUM(Quantity),0) as total FROM `kp_distribute` WHERE Year=%s',[prev_year]):
        distribute_prev_count = distribute_data2.total

    for kp_request_data1 in kp_request.objects.raw('SELECT id, IFNULL(COUNT(purpose), 0) as total FROM `kp_request` WHERE datefortable=%s',[cur_year]):
        request_cur_count = kp_request_data1.total

    for kp_request_data2 in kp_request.objects.raw('SELECT id, IFNULL(COUNT(purpose), 0) as total FROM `kp_request` WHERE datefortable=%s',[prev_year]):
        request_prev_count = kp_request_data2.total

    for kp_total_data1 in kp_input.objects.raw('SELECT id, IFNULL(COUNT(title), 0) as total, datefortable  FROM kp_input WHERE datefortable=%s',[cur_year]):
        kp_cur_count = kp_total_data1.total

    for kp_total_data2 in kp_input.objects.raw('SELECT id, IFNULL(COUNT(title), 0) as total, datefortable  FROM kp_input WHERE datefortable=%s',[prev_year]):
        kp_prev_count = kp_total_data2.total

    for radio_data1 in radio_visitor.objects.raw('SELECT id, IFNULL(COUNT(topic), 0) as segment FROM radio_visitor WHERE year=%s',[cur_year]):
        segment_cur_count = radio_data1.segment

    for radio_data2 in radio_visitor.objects.raw('SELECT id, IFNULL(COUNT(topic), 0) as segment FROM radio_visitor WHERE year=%s',[prev_year]):
        segment_prev_count = radio_data2.segment

    for radio_data3 in radio_visitor.objects.raw('SELECT id, IFNULL(COUNT(sex), 0) as rs FROM radio_visitor WHERE year=%s',[cur_year]):
        rs_cur_count = radio_data3.rs

    for radio_data4 in radio_visitor.objects.raw('SELECT id, IFNULL(COUNT(sex), 0) as rs FROM radio_visitor WHERE year=%s',[prev_year]):
        rs_prev_count = radio_data4.rs

    for radio_data5 in radio_upload.objects.raw('SELECT id, IFNULL(SUM(respondents),0) as respondents FROM radio_upload WHERE year=%s',[cur_year]):
        respondents_cur_count = radio_data5.respondents

    for radio_data6 in radio_upload.objects.raw('SELECT id, IFNULL(SUM(respondents),0) as respondents FROM radio_upload WHERE year=%s',[prev_year]):
        respondents_prev_count = radio_data6.respondents

    for partner_data1 in partners.objects.raw('SELECT id, IFNULL(COUNT(engagement),0) as engagement FROM partners WHERE year=%s',[cur_year]):
        engagement_cur_count = partner_data1.engagement

    for partner_data2 in partners.objects.raw('SELECT id, IFNULL(COUNT(engagement),0) as engagement FROM partners WHERE year=%s',[prev_year]):
        engagement_prev_count = partner_data2.engagement

    context = {
    'dashboard':dashboard,
    'cur_year':cur_year,
    'prev_year':prev_year,
    'awards_count':awards_count,
    'publications_count':publications_count,
    'projects_count':projects_count,
    'staff_count':staff_count,
    'ongoing_project':ongoing_project,
    'staff_active':staff_active,
    'like_cur_count':like_cur_count,
    'like_prev_count':like_prev_count,
    'follow_cur_count':follow_cur_count,
    'follow_prev_count':follow_prev_count,
    'allpost_cur_count':allpost_cur_count,
    'allpost_prev_count':allpost_prev_count,
    'messagesRecieve_cur_count':messagesRecieve_cur_count,
    'responseRate_cur_count':responseRate_cur_count,
    'nSurvey_cur_count':nSurvey_cur_count,
    'messagesRecieve_prev_count':messagesRecieve_prev_count,
    'responseRate_prev_count':responseRate_prev_count,
    'nSurvey_prev_count':nSurvey_prev_count,
    'registered_cur_count':registered_cur_count,
    'registered_prev_count':registered_prev_count,
    'sms_cur_count':sms_cur_count,
    'smsWD_cur_count':smsWD_cur_count,
    'sms_prev_count':sms_prev_count,
    'smsWD_prev_count':smsWD_prev_count,
    'request_cur_count':request_cur_count,
    'request_prev_count':request_prev_count,
    'kp_cur_count':kp_cur_count,
    'kp_prev_count':kp_prev_count,
    'responseptc_cur_count':responseptc_cur_count,
    'responseptc_prev_count':responseptc_prev_count,
    'distribute_cur_count':distribute_cur_count,
    'distribute_prev_count':distribute_prev_count,
    'visit_cur_count':visit_cur_count,
    'visit_prev_count':visit_prev_count,
    'download_cur_count':download_cur_count,
    'download_prev_count':download_prev_count,
    'pageviews_cur_count':pageviews_cur_count,
    'pageviews_prev_count':pageviews_prev_count,
    'pw_visit_cur_count':pw_visit_cur_count,
    'pw_visit_prev_count':pw_visit_prev_count,
    'pw_pageviews_cur_count':pw_pageviews_cur_count,
    'pw_pageviews_prev_count':pw_pageviews_prev_count,
    'pw_stories_cur_count':pw_stories_cur_count,
    'pw_stories_prev_count':pw_stories_prev_count,
    'upload_cur_count':upload_cur_count,
    'upload_prev_count':upload_prev_count,
    'segment_cur_count':segment_cur_count,
    'segment_prev_count':segment_prev_count,
    'rs_cur_count': rs_cur_count,
    'rs_prev_count': rs_prev_count,
    'respondents_cur_count':respondents_cur_count,
    'respondents_prev_count':respondents_prev_count,
    'engagement_cur_count':engagement_cur_count,
    'engagement_prev_count':engagement_prev_count,
    }
    return render(request, 'dashboard/dashboard.html', context)
#data input
#facebook
    #facebook page info
def data_input_fb_page_info(request):
    input_menu_toggle = 'active'
    facebook_input = 'active'
    fb_page_info_form = fb_page_info_Form()
    if request.method == 'POST':
        fb_page_info_form = fb_page_info_Form(request.POST)
        if fb_page_info_form.is_valid():
            fb_page_info_form.save()
            return redirect('/data_input_fb_page_info')

    context = {'fb_page_info_form':fb_page_info_form,
                'facebook_input':facebook_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request, 'dashboard/data_input_fb_page_info.html', context)
def fb_page_infos(request):
    reportndata = 'active'
    facebook_table = 'active'
    page_info = fb_page_info.objects.all()
    context = {
        'page_info':page_info,
        'reportndata': reportndata,
        'facebook_table': facebook_table}
    return render(request,'dashboard/fb_page_info.html', context)
def fb_page_infos_edit(request, pk):
    page_info = fb_page_info.objects.get(pk=pk)
    fb_page_info_form = fb_page_info_Form(instance=page_info)
    if request.method == 'POST':
        fb_page_info_form = fb_page_info_Form(request.POST, instance=page_info)
        if fb_page_info_form.is_valid:
            fb_page_info_form.save()
            return redirect('/fb_page_infos')
    context = {'fb_page_info_form' : fb_page_info_form}
    return render(request, 'dashboard/data_input_fb_page_info.html', context)
def fb_page_infos_delete(request, pk):
    data = fb_page_info.objects.get(pk=pk)
    url = "/fb_page_infos_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/fb_page_infos')
    context = { 'url': url}
    return render(request, 'dashboard/delete.html', context)

def facebook_page_info(request):
    facebook = 'active'
    label = []
    like = []
    follow = []
    seeds = []
    extensions = []
    core = []
    hybrid = []
    pSeeds = []
    pExtensions = []
    pCore = []
    pHybrid = []
    reactions = []
    comments = []
    shares = []
    reach = []
    allpost = []
    videos = []
    vViews = []
    vReactions = []
    vComments = []
    vShares = []
    vReach = []
    vSeeds = []
    vExtensions = []
    vCore = []
    vHybrid = []
    irri = []
    da = []
    ati = []
    pcc = []
    philmech = []
    bpi = []
    bar = []

    labelS = []
    likeS = []
    followS = []
    seedsS = []
    extensionsS = []
    coreS = []
    hybridS = []
    pSeedsS = []
    pExtensionsS = []
    pCoreS = []
    pHybridS = []
    reactionsS = []
    commentsS = []
    sharesS = []
    reachS = []
    allpostS = []
    videosS = []
    vViewsS = []
    vReactionsS = []
    vCommentsS = []
    vSharesS = []
    vReachS = []
    vSeedsS = []
    vExtensionsS = []
    vCoreS = []
    vHybridS = []
    irriS = []
    daS = []
    atiS = []
    pccS = []
    philmechS = []
    bpiS = []
    barS = []

    labelY = []
    likeY = []
    followY = []
    seedsY = []
    extensionsY = []
    coreY = []
    hybridY = []
    pSeedsY = []
    pExtensionsY = []
    pCoreY = []
    pHybridY = []
    reactionsY = []
    commentsY = []
    sharesY = []
    reachY = []
    allpostY = []
    videosY = []
    vViewsY = []
    vReactionsY = []
    vCommentsY = []
    vSharesY = []
    vReachY = []
    vSeedsY = []
    vExtensionsY = []
    vCoreY = []
    vHybridY = []
    irriY = []
    daY = []
    atiY = []
    pccY = []
    philmechY = []
    bpiY = []
    barY = []


    for data in fb_page_info.objects.raw("""SELECT id, CONVERT(SUM(likes), UNSIGNED) as likes, CONVERT(SUM(followers),UNSIGNED) as followers, CONVERT(SUM(seeds),UNSIGNED) as seeds, CONVERT(SUM(extensions),UNSIGNED) as extensions, CONVERT(SUM(core),UNSIGNED) as core, CONVERT(SUM(hybrid),UNSIGNED) as hybrid, CONVERT(SUM(pSeeds), UNSIGNED) as pSeeds, CONVERT(SUM(pExtensions),UNSIGNED) as pExtensions, CONVERT(SUM(pCore), UNSIGNED) as pCore, CONVERT(SUM(pHybrid),UNSIGNED) as pHybrid, CONVERT(SUM(reactions),UNSIGNED) as reactions, CONVERT(SUM(allpost),UNSIGNED) as allpost, CONVERT(SUM(comments),UNSIGNED) as comments, CONVERT(SUM(shares),UNSIGNED) as shares, CONVERT(SUM(reach),UNSIGNED) as reach, CONVERT(SUM(videos),UNSIGNED) as videos, CONVERT(SUM(vViews),UNSIGNED) as vViews, CONVERT(SUM(vReactions),UNSIGNED) as vReactions, CONVERT(SUM(vComments),UNSIGNED) as vComments, CONVERT(SUM(vShares),UNSIGNED) as vShares, CONVERT(SUM(vReach),UNSIGNED) as vReach, CONVERT(SUM(vSeeds),UNSIGNED) as vSeeds, CONVERT(SUM(vExtensions),UNSIGNED) as vExtensions, CONVERT(SUM(vCore),UNSIGNED) as vCore, CONVERT(SUM(vHybrid),UNSIGNED) as vHybrid, CONVERT(SUM(irri),UNSIGNED) as irri, CONVERT(SUM(da),UNSIGNED) as da, CONVERT(SUM(ati),UNSIGNED) as ati, CONVERT(SUM(pcc),UNSIGNED) as pcc, CONVERT(SUM(philmech),UNSIGNED) as philmech, CONVERT(SUM(bpi),UNSIGNED) as bpi, CONVERT(SUM(bar),UNSIGNED) as bar, semester,CONCAT(month,"/",year) as monthyear FROM `fb_page_info` GROUP BY month, year ORDER BY month, year"""):
        label.append(data.monthyear)
        like.append(data.likes)
        follow.append(data.followers)
        seeds.append(data.seeds)
        extensions.append(data.extensions)
        core.append(data.core)
        hybrid.append(data.hybrid)
        pSeeds.append(data.pSeeds)
        pExtensions.append(data.pExtensions)
        pCore.append(data.pCore)
        pHybrid.append(data.pHybrid)
        reactions.append(data.reactions)
        comments.append(data.comments)
        shares.append(data.shares)
        reach.append(data.reach)
        allpost.append(data.allpost)
        videos.append(data.videos)
        vViews.append(data.vViews)
        vReactions.append(data.vReactions)
        vComments.append(data.vComments)
        vShares.append(data.vShares)
        vReach.append(data.vReach)
        vSeeds.append(data.vSeeds)
        vExtensions.append(data.vExtensions)
        vCore.append(data.vCore)
        vHybrid.append(data.vHybrid)
        irri.append(data.vHybrid)
        da.append(data.vHybrid)
        ati.append(data.vHybrid)
        pcc.append(data.vHybrid)
        philmech.append(data.vHybrid)
        bpi.append(data.vHybrid)
        bar.append(data.vHybrid)

    for data in fb_page_info.objects.raw(""" SELECT id, CONVERT(SUM(likes), UNSIGNED) as likes, CONVERT(SUM(followers),UNSIGNED) as followers, CONVERT(SUM(seeds),UNSIGNED) as seeds, CONVERT(SUM(extensions),UNSIGNED) as extensions, CONVERT(SUM(core),UNSIGNED) as core, CONVERT(SUM(hybrid),UNSIGNED) as hybrid, CONVERT(SUM(pSeeds), UNSIGNED) as pSeeds, CONVERT(SUM(pExtensions),UNSIGNED) as pExtensions, CONVERT(SUM(pCore), UNSIGNED) as pCore, CONVERT(SUM(pHybrid),UNSIGNED) as pHybrid, CONVERT(SUM(reactions),UNSIGNED) as reactions, CONVERT(SUM(allpost),UNSIGNED) as allpost, CONVERT(SUM(comments),UNSIGNED) as comments, CONVERT(SUM(shares),UNSIGNED) as shares, CONVERT(SUM(reach),UNSIGNED) as reach, CONVERT(SUM(videos),UNSIGNED) as videos, CONVERT(SUM(vViews),UNSIGNED) as vViews, CONVERT(SUM(vReactions),UNSIGNED) as vReactions, CONVERT(SUM(vComments),UNSIGNED) as vComments, CONVERT(SUM(vShares),UNSIGNED) as vShares, CONVERT(SUM(vReach),UNSIGNED) as vReach, CONVERT(SUM(vSeeds),UNSIGNED) as vSeeds, CONVERT(SUM(vExtensions),UNSIGNED) as vExtensions, CONVERT(SUM(vCore),UNSIGNED) as vCore, CONVERT(SUM(vHybrid),UNSIGNED) as vHybrid, CONVERT(SUM(irri),UNSIGNED) as irri, CONVERT(SUM(da),UNSIGNED) as da, CONVERT(SUM(ati),UNSIGNED) as ati, CONVERT(SUM(pcc),UNSIGNED) as pcc, CONVERT(SUM(philmech),UNSIGNED) as philmech, CONVERT(SUM(bpi),UNSIGNED) as bpi, CONVERT(SUM(bar),UNSIGNED) as bar, CONCAT(semester,"S ",year) as semyr FROM `fb_page_info` GROUP BY semester,year ORDER BY semester,year"""):
        labelS.append(data.semyr)
        likeS.append(data.likes)
        followS.append(data.followers)
        seedsS.append(data.seeds)
        extensionsS.append(data.extensions)
        coreS.append(data.core)
        hybridS.append(data.hybrid)
        pSeedsS.append(data.pSeeds)
        pExtensionsS.append(data.pExtensions)
        pCoreS.append(data.pCore)
        pHybridS.append(data.pHybrid)
        reactionsS.append(data.reactions)
        commentsS.append(data.comments)
        sharesS.append(data.shares)
        reachS.append(data.reach)
        allpostS.append(data.allpost)
        videosS.append(data.videos)
        vViewsS.append(data.vViews)
        vReactionsS.append(data.vReactions)
        vCommentsS.append(data.vComments)
        vSharesS.append(data.vShares)
        vReachS.append(data.vReach)
        vSeedsS.append(data.vSeeds)
        vExtensionsS.append(data.vExtensions)
        vCoreS.append(data.vCore)
        vHybridS.append(data.vHybrid)
        irriS.append(data.vHybrid)
        daS.append(data.vHybrid)
        atiS.append(data.vHybrid)
        pccS.append(data.vHybrid)
        philmechS.append(data.vHybrid)
        bpiS.append(data.vHybrid)
        barS.append(data.vHybrid)

    for data in fb_page_info.objects.raw(""" SELECT id, CONVERT(SUM(likes), UNSIGNED) as likes, CONVERT(SUM(followers),UNSIGNED) as followers, CONVERT(SUM(seeds),UNSIGNED) as seeds, CONVERT(SUM(extensions),UNSIGNED) as extensions, CONVERT(SUM(core),UNSIGNED) as core, CONVERT(SUM(hybrid),UNSIGNED) as hybrid, CONVERT(SUM(pSeeds), UNSIGNED) as pSeeds, CONVERT(SUM(pExtensions),UNSIGNED) as pExtensions, CONVERT(SUM(pCore), UNSIGNED) as pCore, CONVERT(SUM(pHybrid),UNSIGNED) as pHybrid, CONVERT(SUM(reactions),UNSIGNED) as reactions, CONVERT(SUM(allpost),UNSIGNED) as allpost, CONVERT(SUM(comments),UNSIGNED) as comments, CONVERT(SUM(shares),UNSIGNED) as shares, CONVERT(SUM(reach),UNSIGNED) as reach, CONVERT(SUM(videos),UNSIGNED) as videos, CONVERT(SUM(vViews),UNSIGNED) as vViews, CONVERT(SUM(vReactions),UNSIGNED) as vReactions, CONVERT(SUM(vComments),UNSIGNED) as vComments, CONVERT(SUM(vShares),UNSIGNED) as vShares, CONVERT(SUM(vReach),UNSIGNED) as vReach, CONVERT(SUM(vSeeds),UNSIGNED) as vSeeds, CONVERT(SUM(vExtensions),UNSIGNED) as vExtensions, CONVERT(SUM(vCore),UNSIGNED) as vCore, CONVERT(SUM(vHybrid),UNSIGNED) as vHybrid, CONVERT(SUM(irri),UNSIGNED) as irri, CONVERT(SUM(da),UNSIGNED) as da, CONVERT(SUM(ati),UNSIGNED) as ati, CONVERT(SUM(pcc),UNSIGNED) as pcc, CONVERT(SUM(philmech),UNSIGNED) as philmech, CONVERT(SUM(bpi),UNSIGNED) as bpi, CONVERT(SUM(bar),UNSIGNED) as bar, year FROM `fb_page_info` GROUP BY year ORDER BY year """):
        labelY.append(data.year)
        likeY.append(data.likes)
        followY.append(data.followers)
        seedsY.append(data.seeds)
        extensionsY.append(data.extensions)
        coreY.append(data.core)
        hybridY.append(data.hybrid)
        pSeedsY.append(data.pSeeds)
        pExtensionsY.append(data.pExtensions)
        pCoreY.append(data.pCore)
        pHybridY.append(data.pHybrid)
        reactionsY.append(data.reactions)
        commentsY.append(data.comments)
        sharesY.append(data.shares)
        reachY.append(data.reach)
        allpostY.append(data.allpost)
        videosY.append(data.videos)
        vViewsY.append(data.vViews)
        vReactionsY.append(data.vReactions)
        vCommentsY.append(data.vComments)
        vSharesY.append(data.vShares)
        vReachY.append(data.vReach)
        vSeedsY.append(data.vSeeds)
        vExtensionsY.append(data.vExtensions)
        vCoreY.append(data.vCore)
        vHybridY.append(data.vHybrid)
        irriY.append(data.vHybrid)
        daY.append(data.vHybrid)
        atiY.append(data.vHybrid)
        pccY.append(data.vHybrid)
        philmechY.append(data.vHybrid)
        bpiY.append(data.vHybrid)
        barY.append(data.vHybrid)

    context = {
    'facebook':facebook,
    'label':label,
    'like':like,
    'follow':follow,
    'seeds': seeds,
    'extensions': extensions,
    'core': core,
    'hybrid': hybrid,
    'pSeeds':pSeeds,
    'pExtensions':pExtensions,
    'pCore':pCore,
    'pHybrid':pHybrid,
    'reactions': reactions,
    'comments': comments,
    'shares': shares,
    'reach': reach,
    'allpost': allpost,
    'videos': videos,
    'vViews':vViews,
    'vReactions':vReactions,
    'vComments':vComments,
    'vShares':vShares,
    'vReach':vReach,
    'vSeeds':vSeeds,
    'vExtensions':vExtensions,
    'vCore':vCore,
    'vHybrid':vHybrid,
    'irri':irri,
    'da':da,
    'ati':ati,
    'pcc':pcc,
    'philmech':philmech,
    'bpi':bpi,
    'bar':bar,

    'labelS': labelS,
    'likeS': likeS,
    'followS': followS,
    'seedsS': seedsS,
    'extensionsS': extensionsS,
    'coreS': coreS,
    'hybridS': hybridS,
    'pSeedsS':pSeedsS,
    'pExtensionsS':pExtensionsS,
    'pCoreS':pCoreS,
    'pHybridS':pHybridS,
    'reactionsS': reactionsS,
    'commentsS': commentsS,
    'sharesS': sharesS,
    'reachS': reachS,
    'allpostS': allpostS,
    'videosS': videosS,
    'vViewsS':vViews,
    'vReactionsS':vReactionsS,
    'vCommentsS':vCommentsS,
    'vSharesS':vSharesS,
    'vReachS':vReachS,
    'vSeedsS':vSeeds,
    'vExtensionsS':vExtensionsS,
    'vCoreS':vCoreS,
    'vHybridS':vHybridS,
    'irriS':irriS,
    'daS':daS,
    'atiS':atiS,
    'pccS':pccS,
    'philmechS':philmechS,
    'bpiS':bpiS,
    'barS':barS,

    'labelY': labelY,
    'likeY': likeY,
    'followY': followY,
    'seedsY': seedsY,
    'extensionsY': extensionsY,
    'coreY': coreY,
    'hybridY': hybridY,
    'pSeedsY':pSeedsY,
    'pExtensionsY':pExtensionsY,
    'pCoreY':pCoreY,
    'pHybridY':pHybridY,
    'reactionsY': reactionsY,
    'commentsY': commentsY,
    'sharesY': sharesY,
    'reachY': reachY,
    'allpostY': allpostY,
    'videosY': videosY,
    'vViewsY':vViewsY,
    'vReactionsY':vReactionsY,
    'vCommentsY':vCommentsY,
    'vSharesY':vSharesY,
    'vReachY':vReachY,
    'vSeedsY':vSeedsY,
    'vExtensionsY':vExtensionsY,
    'vCoreY':vCoreY,
    'vHybridY':vHybridY,
    'irriY':irriY,
    'daY':daY,
    'atiY':atiY,
    'pccY':pccY,
    'philmechY':philmechY,
    'bpiY':bpiY,
    'barY':barY,
    }
    return render(request,'dashboard/facebook_page_info.html',context)
    #end facebook page info
    #facebook post data
def data_input_fb_post_data(request):
    input_menu_toggle = 'active'
    facebook_input = 'active'
    fb_post_data_form = fb_post_data_Form()
    if request.method == 'POST':
        fb_post_data_form = fb_post_data_Form(request.POST)
        if fb_post_data_form.is_valid():
            fb_post_data_form.save()
            return redirect('/data_input_fb_post_data')

    context = {'fb_post_data_form':fb_post_data_form,
                'facebook_input':facebook_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request, 'dashboard/data_input_fb_post_data.html', context)
def fb_posts_data(request):
    reportndata = 'active'
    facebook_table = 'active'
    post_data = fb_post_data.objects.all()
    context = {'post_data':post_data,
    'reportndata': reportndata,
    'facebook_table': facebook_table}
    return render(request, 'dashboard/fb_post_data.html', context)
def fb_posts_data_edit(request, pk):
    post_data = fb_post_data.objects.get(pk=pk)
    fb_post_data_form = fb_post_data_Form(instance=post_data)
    if request.method == 'POST':
        fb_post_data_form = fb_post_data_Form(request.POST, instance=post_data)
        if fb_post_data_form.is_valid:
            fb_post_data_form.save()
            return redirect('/fb_post_data')
    context = {'fb_post_data_form':fb_post_data_form}
    return render(request, 'dashboard/data_input_fb_post_data.html', context)
def fb_posts_data_delete(request, pk):
    data = fb_post_data.objects.get(pk=pk)
    url = "/fb_post_data_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/fb_post_data')
    context = { 'url': url}
    return render(request, 'dashboard/delete.html', context)
    #end facebook post data
    #facebook post comments

def facebook_post_data(request):
    facebook = 'active'
    label = []
    responseRate = []
    messagesRecieve = []
    nSurvey = []
    male = []
    female = []
    nSurveyYes1 = []
    nSurveyNo1 = []
    nSurveyYes2 = []
    nSurveyNo2 = []

    labelS = []
    responseRateS = []
    messagesRecieveS = []
    nSurveyS = []
    maleS = []
    femaleS = []
    nSurveyYes1S = []
    nSurveyNo1S = []
    nSurveyYes2S = []
    nSurveyNo2S = []

    labelY=[]
    responseRateY = []
    nSurveyY = []
    messagesRecieveY = []
    maleY = []
    femaleY = []
    nSurveyYes1Y = []
    nSurveyNo1Y = []
    nSurveyYes2Y = []
    nSurveyNo2Y = []

    toptopics = fb_post_data.objects.raw(""" SELECT id, topic1 AS topic, ntopic1 AS total, month, year FROM fb_post_data GROUP BY topic1, month, year UNION ALL SELECT id, topic2, ntopic2, month, year FROM fb_post_data GROUP BY topic2, month, year UNION ALL SELECT id, topic3, ntopic3, month, year FROM fb_post_data GROUP BY topic3, month, year UNION ALL SELECT id, topic4, ntopic4, month, year FROM fb_post_data GROUP BY topic4, month, year UNION ALL SELECT id, topic5, ntopic5, month, year FROM fb_post_data GROUP BY topic5, month, year ORDER BY total DESC, month DESC, year DESC """)
    topoccupation = fb_post_data.objects.raw(""" SELECT id, occupation1 AS occupation, noccupation1 AS total, month, year FROM fb_post_data GROUP BY occupation1, month, year UNION ALL SELECT id, occupation2, noccupation2, month, year FROM fb_post_data GROUP BY occupation2, month, year UNION ALL SELECT id, occupation3, noccupation3, month, year FROM fb_post_data GROUP BY occupation3, month, year UNION ALL SELECT id, occupation4, noccupation4, month, year FROM fb_post_data GROUP BY occupation4, month, year UNION ALL SELECT id, occupation5, noccupation5, month, year FROM fb_post_data GROUP BY occupation5, month, year ORDER BY total DESC, month DESC, year DESC """)

    for data in fb_post_data.objects.raw(""" SELECT id, CONVERT(SUM(responseRate),UNSIGNED) as responseRate, CONVERT(SUM(messagesRecieve),UNSIGNED) as messagesRecieve, CONVERT(SUM(nSurvey),UNSIGNED) as nSurvey, CONVERT(SUM(male), UNSIGNED) as male, CONVERT(SUM(female), UNSIGNED) as female, CONVERT(SUM(nSurveyYes1),UNSIGNED) as nSurveyYes1, CONVERT(SUM(nSurveyNo1),UNSIGNED) as nSurveyNo1, CONVERT(SUM(nSurveyYes2),UNSIGNED) as nSurveyYes2, CONVERT(SUM(nSurveyNo2),UNSIGNED) as nSurveyNo2, CONCAT(month,"/",year) as monthyear FROM fb_post_data GROUP BY month, year ORDER BY year,month """):
        label.append(data.monthyear)
        responseRate.append(data.responseRate)
        messagesRecieve.append(data.messagesRecieve)
        nSurvey.append(data.nSurvey)
        male.append(data.male)
        female.append(data.female)
        nSurveyYes1.append(data.nSurveyYes1)
        nSurveyNo1.append(data.nSurveyNo1)
        nSurveyYes2.append(data.nSurveyYes2)
        nSurveyNo2.append(data.nSurveyNo2)

    for data in fb_post_data.objects.raw(""" SELECT id, CONVERT(SUM(responseRate),UNSIGNED) as responseRate, CONVERT(SUM(messagesRecieve),UNSIGNED) as messagesRecieve, CONVERT(SUM(nSurvey),UNSIGNED) as nSurvey, CONVERT(SUM(male), UNSIGNED) as male, CONVERT(SUM(female), UNSIGNED) as female, CONVERT(SUM(nSurveyYes1),UNSIGNED) as nSurveyYes1, CONVERT(SUM(nSurveyNo1),UNSIGNED) as nSurveyNo1, CONVERT(SUM(nSurveyYes2),UNSIGNED) as nSurveyYes2, CONVERT(SUM(nSurveyNo2),UNSIGNED) as nSurveyNo2, CONCAT(semester,"S ",year) as semyear FROM fb_post_data GROUP BY semester, year ORDER BY year, semester """):
        labelS.append(data.semyear)
        responseRateS.append(data.responseRate)
        messagesRecieveS.append(data.messagesRecieve)
        nSurveyS.append(data.nSurvey)
        maleS.append(data.male)
        femaleS.append(data.female)
        nSurveyYes1S.append(data.nSurveyYes1)
        nSurveyNo1S.append(data.nSurveyNo1)
        nSurveyYes2S.append(data.nSurveyYes2)
        nSurveyNo2S.append(data.nSurveyNo2)

    for data in fb_post_data.objects.raw(""" SELECT id, CONVERT(SUM(responseRate),UNSIGNED) as responseRate, CONVERT(SUM(messagesRecieve),UNSIGNED) as messagesRecieve, CONVERT(SUM(nSurvey),UNSIGNED) as nSurvey, CONVERT(SUM(male), UNSIGNED) as male, CONVERT(SUM(female), UNSIGNED) as female, CONVERT(SUM(nSurveyYes1),UNSIGNED) as nSurveyYes1, CONVERT(SUM(nSurveyNo1),UNSIGNED) as nSurveyNo1, CONVERT(SUM(nSurveyYes2),UNSIGNED) as nSurveyYes2, CONVERT(SUM(nSurveyNo2),UNSIGNED) as nSurveyNo2, year FROM fb_post_data GROUP BY year ORDER BY year """):
        labelY.append(data.year)
        responseRateY.append(data.responseRate)
        messagesRecieveY.append(data.messagesRecieve)
        nSurveyY.append(data.nSurvey)
        maleY.append(data.male)
        femaleY.append(data.female)
        nSurveyYes1Y.append(data.nSurveyYes1)
        nSurveyNo1Y.append(data.nSurveyNo1)
        nSurveyYes2Y.append(data.nSurveyYes2)
        nSurveyNo2Y.append(data.nSurveyNo2)




    context = {
    'facebook':facebook,
    'toptopics': toptopics,
    'topoccupation':topoccupation,
    'label':label,
    'responseRate': responseRate,
    'messagesRecieve': messagesRecieve,
    'nSurvey':nSurvey,
    'male': male,
    'female': female,
    'nSurveyYes1':nSurveyYes1,
    'nSurveyNo1':nSurveyNo1,
    'nSurveyYes2':nSurveyYes2,
    'nSurveyNo2':nSurveyNo2,

    'labelS':labelS,
    'responseRateS': responseRateS,
    'messagesRecieveS': messagesRecieveS,
    'nSurveyS':nSurveyS,
    'maleS': maleS,
    'femaleS': femaleS,
    'nSurveyYes1S':nSurveyYes1S,
    'nSurveyNo1S':nSurveyNo1S,
    'nSurveyYes2S':nSurveyYes2S,
    'nSurveyNo2S':nSurveyNo2S,

    'labelY':labelY,
    'responseRateY': responseRateY,
    'messagesRecieveY': messagesRecieveY,
    'nSurveyY':nSurveyY,
    'maleY': maleY,
    'femaleY': femaleY,
    'nSurveyYes1Y':nSurveyYes1Y,
    'nSurveyNo1Y':nSurveyNo1Y,
    'nSurveyYes2Y':nSurveyYes2Y,
    'nSurveyNo2Y':nSurveyNo2Y,
    }
    return render(request,'dashboard/facebook_post_data.html',context)
#end facbook
#PhilRice Text Center
def data_input_ptc(request):
    input_menu_toggle = 'active'
    ptc_input = 'active'
    ptc_form = ptc_Form()
    if request.method == 'POST':
        ptc_form = ptc_Form(request.POST)
        if ptc_form.is_valid():
            ptc_form.save()
            return redirect('/data_input_ptc')

    context = {'ptc_form':ptc_form,
                'ptc_input':ptc_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request, 'dashboard/data_input_ptc.html', context)

def ptcs(request):
    reportndata = 'active'
    ptc_table = 'active'
    text = ptc.objects.all()
    context = {'text':text,
    'reportndata':reportndata,
    'ptc_table':ptc_table}
    return render(request, 'dashboard/ptc_data.html', context)

def philricetextcenter(request):
    ptcs = 'active'
    ptc_year = []
    id = []
    sms = []
    smsWD = []
    smsWE = []
    texterOH = []
    texterNOH = []
    texterWD = []
    texterWE = []
    keywords = []
    male = []
    female = []

    yr2017_data = []
    yr2018_data = []
    yr2019_data = []
    yr2020_data = []
    yr2021_data = []

    total_location=[]
    year_location=[]

    OH1to15 = []
    OH16to1h = []
    OH1hto4h = []
    OH4hto12h = []
    OH12up = []
    OHyear = []

    NOH1to15 = []
    NOH16to1h = []
    NOH1hto4h = []
    NOH4hto12h = []
    NOH12up = []
    NOHyear = []

    WOH1to15 = []
    WOH16to1h = []
    WOH1hto4h = []
    WOH4hto12h = []
    WOH12up = []
    WOHyear = []

    location = ptc.objects.raw(""" SELECT id, SUM(abra) as total, month, year, 'Abra' description from ptc GROUP BY year UNION ALL SELECT id, SUM(agusanNorte),month, year, 'Agusan del Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(agusanSur),month, year, 'Agusan del Sur' description from ptc GROUP BY year UNION ALL SELECT id, SUM(aklan),month, year, 'Aklan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(albay),month, year, 'Albay' description from ptc GROUP BY year UNION ALL SELECT id, SUM(antique),month, year, 'Antique' description from ptc GROUP BY year UNION ALL SELECT id, SUM(apayao),month, year, 'Apayao' description from ptc GROUP BY year UNION ALL SELECT id, SUM(aurora),month, year, 'Aurora' description from ptc GROUP BY year UNION ALL SELECT id, SUM(basilan),month, year, 'Basilan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(bataan),month, year, 'Bataan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(batanes),month, year, 'Batanes' description from ptc GROUP BY year UNION ALL SELECT id, SUM(benguet),month, year, 'Benguet' description from ptc GROUP BY year UNION ALL SELECT id, SUM(biliran),month, year, 'Biliran' description from ptc GROUP BY year UNION ALL SELECT id, SUM(bohol),month, year, 'Bohol' description from ptc GROUP BY year UNION ALL SELECT id, SUM(bukidnon),month, year, 'Bukidnon' description from ptc GROUP BY year UNION ALL SELECT id, SUM(bulacan),month, year, 'Bulacan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(cagayan),month, year, 'Cagayan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(camarinesNorte),month, year, 'Camarines Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(camarinesSur),month, year, 'Camarines Sur' description from ptc GROUP BY year UNION ALL SELECT id, SUM(camiguin),month, year, 'Camiguin' description from ptc GROUP BY year UNION ALL SELECT id, SUM(capiz),month, year, 'Capiz' description from ptc GROUP BY year UNION ALL SELECT id, SUM(catanduanes),month, year, 'Catanduanes' description from ptc GROUP BY year UNION ALL SELECT id, SUM(cavite),month, year, 'Cavite' description from ptc GROUP BY year UNION ALL SELECT id, SUM(cebu),month, year, 'Cebu' description from ptc GROUP BY year UNION ALL SELECT id, SUM(compostela),month, year, 'Compostela Valley' description from ptc GROUP BY year UNION ALL SELECT id, SUM(davaoNorte),month, year, 'Davao del Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(davaoSur),month, year, 'Davao del Sur' description from ptc GROUP BY year UNION ALL SELECT id, SUM(davaoOriental),month, year, 'Davao Oriental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(samarEast),month, year, 'Eastern Samar' description from ptc GROUP BY year UNION ALL SELECT id, SUM(guimaras),month, year, 'Guimaras' description from ptc GROUP BY year UNION ALL SELECT id, SUM(ifugao),month, year, 'Ifugao' description from ptc GROUP BY year UNION ALL SELECT id, SUM(ilocosNorte),month, year, 'Ilocos Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(ilocosSur),month, year, 'Ilocos Sur' description from ptc GROUP BY year UNION ALL SELECT id, SUM(iloilo),month, year, 'Iloilo' description from ptc GROUP BY year UNION ALL SELECT id, SUM(isabela),month, year, 'Isabela' description from ptc GROUP BY year UNION ALL SELECT id, SUM(kalinga),month, year, 'Kalinga' description from ptc GROUP BY year UNION ALL SELECT id, SUM(launion),month, year, 'La Union' description from ptc GROUP BY year UNION ALL SELECT id, SUM(lanaoNorte),month, year, 'Lanao Del Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(lanaoSur),month, year, 'Lanao Del Sur' description from ptc GROUP BY year UNION ALL SELECT id, SUM(leyte),month, year, 'Leyte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(maguindanao),month, year, 'Maguindanao' description from ptc GROUP BY year UNION ALL SELECT id, SUM(marinduque),month, year, 'Marinduque' description from ptc GROUP BY year UNION ALL SELECT id, SUM(masbate),month, year, 'Masbate' description from ptc GROUP BY year UNION ALL SELECT id, SUM(manila),month, year, 'Metro Manila' description from ptc GROUP BY year UNION ALL SELECT id, SUM(misamisOccidental),month, year, 'Misamis Occidental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(misamisOriental),month, year, 'Misamis Oriental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(mountainProvince),month, year, 'Mountain Province' description from ptc GROUP BY year UNION ALL SELECT id, SUM(negrosOccidental),month, year, 'Negros Occidental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(negrosOriental),month, year, 'Negros Oriental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(cotabatoNorth),month, year, 'Northern Cotabato' description from ptc GROUP BY year UNION ALL SELECT id, SUM(samarNorth),month, year, 'Northern Samar' description from ptc GROUP BY year UNION ALL SELECT id, SUM(nuevaEcija),month, year, 'Nueva Ecija' description from ptc GROUP BY year UNION ALL SELECT id, SUM(nuevaVizcaya),month, year, 'Nueva Vizcaya' description from ptc GROUP BY year UNION ALL SELECT id, SUM(mindoroOccidental),month, year, 'Mindoro Occidental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(mindoroOriental),month, year, 'Mindoro Oriental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(palawan),month, year, 'Palawan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(pangasinan),month, year, 'Pangasinan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(quezon),month, year, 'Quezon' description from ptc GROUP BY year UNION ALL SELECT id, SUM(quirino),month, year, 'Quirino' description from ptc GROUP BY year UNION ALL SELECT id, SUM(rizal),month, year, 'Rizal' description from ptc GROUP BY year UNION ALL SELECT id, SUM(romblon),month, year, 'Romblon' description from ptc GROUP BY year UNION ALL SELECT id, SUM(samar),month, year, 'Samar' description from ptc GROUP BY year UNION ALL SELECT id, SUM(sarangani),month, year, 'Sarangani' description from ptc GROUP BY year UNION ALL SELECT id, SUM(siquijor),month, year, 'Siquijor' description from ptc GROUP BY year UNION ALL SELECT id, SUM(sorsogon),month, year, 'Sorsogon' description from ptc GROUP BY year UNION ALL SELECT id, SUM(cotabatoSouth),month, year, 'South Cotabato' description from ptc GROUP BY year UNION ALL SELECT id, SUM(leyteSouth),month, year, 'Southern Leyte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(sultanKudarat),month, year, 'Sultan Kudarat' description from ptc GROUP BY year UNION ALL SELECT id, SUM(sulu),month, year, 'Sulu' description from ptc GROUP BY year UNION ALL SELECT id, SUM(surigaoNorte),month, year, 'Surigao Del Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(surigaoSur),month, year, 'Surigao Del Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(tarlac),month, year, 'Tarlac' description from ptc GROUP BY year UNION ALL SELECT id, SUM(tawitawi),month, year, 'Tawi-tawi' description from ptc GROUP BY year UNION ALL SELECT id, SUM(zambales),month, year, 'Zambales' description from ptc GROUP BY year UNION ALL SELECT id, SUM(zamboangaNorte),month, year, 'Zamboanga Del Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(zamboangaSibugay),month, year, 'Zamboanga Sibugay' description from ptc GROUP BY year UNION ALL SELECT id, SUM(zamboangaSur),month, year, 'Zamboanga Del Sur' description from ptc GROUP BY year UNION ALL SELECT id, SUM(international),month, year, 'International' description from ptc GROUP BY year UNION ALL SELECT id, SUM(undetermined),month, year, 'Undetermined' description from ptc GROUP BY year ORDER BY `total`  DESC """)

    sms_yr = ptc.objects.raw("""SELECT id, SUM(seedAvail) as total, month, year, 'Seed Availablity' description from ptc GROUP BY year UNION ALL SELECT id, SUM(seedVar) as total, month, year, 'Seed Quality and Varietal Info' description from ptc GROUP BY year UNION ALL SELECT id, SUM(landPrep) as total, month, year, 'Land Preparation' description from ptc GROUP BY year UNION ALL SELECT id, SUM(cropEsta) as total, month, year, 'Crop Establishment' description from ptc GROUP BY year UNION ALL SELECT id, SUM(nutriMng) as total, month, year, 'Nutrient Management' description from ptc GROUP BY year UNION ALL SELECT id, SUM(waterMng) as total, month, year, 'Water Management' description from ptc GROUP BY year UNION ALL SELECT id, SUM(pestMng) as total, month, year, 'Pest Management' description from ptc GROUP BY year UNION ALL SELECT id, SUM(harvMng) as total, month, year, 'Harvest & Post-harvest Management' description from ptc GROUP BY year UNION ALL SELECT id, SUM(genInfo) as total, month, year, 'General Info/Research' description from ptc GROUP BY year UNION ALL SELECT id, SUM(knowProd) as total, month, year, 'Knowledge Products' description from ptc GROUP BY year UNION ALL SELECT id, SUM(machine) as total, month, year, 'Machines' description from ptc GROUP BY year UNION ALL SELECT id, SUM(foodSci) as total, month, year, 'Food Science' description from ptc GROUP BY year UNION ALL SELECT id, SUM(training) as total, month, year, 'Training' description from ptc GROUP BY year UNION ALL SELECT id, SUM(palayamanan) as total, month, year, 'Palayamanan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(philrice) as total, month, year, 'PhilRice' description from ptc GROUP BY year UNION ALL SELECT id, SUM(otherAgency) as total, month, year, 'Other Agencies' description from ptc GROUP BY year UNION ALL SELECT id, SUM(greetings) as total, month, year, 'Greetings' description from ptc GROUP BY year UNION ALL SELECT id, SUM(thanks) as total, month, year, 'Thanks' description from ptc GROUP BY year UNION ALL SELECT id, SUM(registration) as total, month, year, 'Registration' description from ptc GROUP BY year UNION ALL SELECT id, SUM(others) as total, month, year, 'Unrelated/Others' description from ptc GROUP BY year UNION ALL SELECT id, SUM(RCEF) as total, month, year, 'RCEF' description from ptc GROUP BY year UNION ALL SELECT id, SUM(rcefSeed) as total, month, year, 'RCEF Seeds' description from ptc GROUP BY year UNION ALL SELECT id, SUM(rcefComp) as total, month, year, 'RCEF Complains' description from ptc GROUP BY year UNION ALL SELECT id, SUM(rcefExt) as total, month, year, 'RCEF Extensions' description from ptc GROUP BY year UNION ALL SELECT id, SUM(rsbsa) as total, month, year, 'RSBSA' description from ptc GROUP BY year UNION ALL SELECT id, SUM(website) as total, month, year, 'Website Promotion' description from ptc GROUP BY year""")

    # need to add data annually
    # start
    for data in ptc.objects.raw(""" SELECT id, month, year, sms FROM ptc WHERE year="2017" GROUP BY month, year """):
        yr2017_data.append(data.sms)
    for data in ptc.objects.raw(""" SELECT id, month, year, sms FROM ptc WHERE year="2018" GROUP BY month, year """):
        yr2018_data.append(data.sms)
    for data in ptc.objects.raw(""" SELECT id, month, year, sms FROM ptc WHERE year="2019" GROUP BY month, year """):
        yr2019_data.append(data.sms)
    for data in ptc.objects.raw(""" SELECT id, month, year, sms FROM ptc WHERE year="2020" GROUP BY month, year """):
        yr2020_data.append(data.sms)
    for data in ptc.objects.raw(""" SELECT id, month, year, sms FROM ptc WHERE year="2021" GROUP BY month, year """):
        yr2021_data.append(data.sms)
    # end

    for total_year in ptc.objects.raw(""" SELECT id, CONVERT(SUM(total), UNSIGNED) as total, month, year FROM(
    SELECT id, SUM(abra) as total, month, year, 'Abra' description from ptc GROUP BY year UNION ALL SELECT id, SUM(agusanNorte),month, year, 'Agusan del Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(agusanSur),month, year, 'Agusan del Sur' description from ptc GROUP BY year UNION ALL SELECT id, SUM(aklan),month, year, 'Aklan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(albay),month, year, 'Albay' description from ptc GROUP BY year UNION ALL SELECT id, SUM(antique),month, year, 'Antique' description from ptc GROUP BY year UNION ALL SELECT id, SUM(apayao),month, year, 'Apayao' description from ptc GROUP BY year UNION ALL SELECT id, SUM(aurora),month, year, 'Aurora' description from ptc GROUP BY year UNION ALL SELECT id, SUM(basilan),month, year, 'Basilan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(bataan),month, year, 'Bataan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(batanes),month, year, 'Batanes' description from ptc GROUP BY year UNION ALL SELECT id, SUM(benguet),month, year, 'Benguet' description from ptc GROUP BY year UNION ALL SELECT id, SUM(biliran),month, year, 'Biliran' description from ptc GROUP BY year UNION ALL SELECT id, SUM(bohol),month, year, 'Bohol' description from ptc GROUP BY year UNION ALL SELECT id, SUM(bukidnon),month, year, 'Bukidnon' description from ptc GROUP BY year UNION ALL SELECT id, SUM(bulacan),month, year, 'Bulacan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(cagayan),month, year, 'Cagayan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(camarinesNorte),month, year, 'Camarines Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(camarinesSur),month, year, 'Camarines Sur' description from ptc GROUP BY year UNION ALL SELECT id, SUM(camiguin),month, year, 'Camiguin' description from ptc GROUP BY year UNION ALL SELECT id, SUM(capiz),month, year, 'Capiz' description from ptc GROUP BY year UNION ALL SELECT id, SUM(catanduanes),month, year, 'Catanduanes' description from ptc GROUP BY year UNION ALL SELECT id, SUM(cavite),month, year, 'Cavite' description from ptc GROUP BY year UNION ALL SELECT id, SUM(cebu),month, year, 'Cebu' description from ptc GROUP BY year UNION ALL SELECT id, SUM(compostela),month, year, 'Compostela Valley' description from ptc GROUP BY year UNION ALL SELECT id, SUM(davaoNorte),month, year, 'Davao del Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(davaoSur),month, year, 'Davao del Sur' description from ptc GROUP BY year UNION ALL SELECT id, SUM(davaoOriental),month, year, 'Davao Oriental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(samarEast),month, year, 'Eastern Samar' description from ptc GROUP BY year UNION ALL SELECT id, SUM(guimaras),month, year, 'Guimaras' description from ptc GROUP BY year UNION ALL SELECT id, SUM(ifugao),month, year, 'Ifugao' description from ptc GROUP BY year UNION ALL SELECT id, SUM(ilocosNorte),month, year, 'Ilocos Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(ilocosSur),month, year, 'Ilocos Sur' description from ptc GROUP BY year UNION ALL SELECT id, SUM(iloilo),month, year, 'Iloilo' description from ptc GROUP BY year UNION ALL SELECT id, SUM(isabela),month, year, 'Isabela' description from ptc GROUP BY year UNION ALL SELECT id, SUM(kalinga),month, year, 'Kalinga' description from ptc GROUP BY year UNION ALL SELECT id, SUM(launion),month, year, 'La Union' description from ptc GROUP BY year UNION ALL SELECT id, SUM(lanaoNorte),month, year, 'Lanao Del Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(lanaoSur),month, year, 'Lanao Del Sur' description from ptc GROUP BY year UNION ALL SELECT id, SUM(leyte),month, year, 'Leyte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(maguindanao),month, year, 'Maguindanao' description from ptc GROUP BY year UNION ALL SELECT id, SUM(marinduque),month, year, 'Marinduque' description from ptc GROUP BY year UNION ALL SELECT id, SUM(masbate),month, year, 'Masbate' description from ptc GROUP BY year UNION ALL SELECT id, SUM(manila),month, year, 'Metro Manila' description from ptc GROUP BY year UNION ALL SELECT id, SUM(misamisOccidental),month, year, 'Misamis Occidental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(misamisOriental),month, year, 'Misamis Oriental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(mountainProvince),month, year, 'Mountain Province' description from ptc GROUP BY year UNION ALL SELECT id, SUM(negrosOccidental),month, year, 'Negros Occidental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(negrosOriental),month, year, 'Negros Oriental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(cotabatoNorth),month, year, 'Northern Cotabato' description from ptc GROUP BY year UNION ALL SELECT id, SUM(samarNorth),month, year, 'Northern Samar' description from ptc GROUP BY year UNION ALL SELECT id, SUM(nuevaEcija),month, year, 'Nueva Ecija' description from ptc GROUP BY year UNION ALL SELECT id, SUM(nuevaVizcaya),month, year, 'Nueva Vizcaya' description from ptc GROUP BY year UNION ALL SELECT id, SUM(mindoroOccidental),month, year, 'Mindoro Occidental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(mindoroOriental),month, year, 'Mindoro Oriental' description from ptc GROUP BY year UNION ALL SELECT id, SUM(palawan),month, year, 'Palawan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(pangasinan),month, year, 'Pangasinan' description from ptc GROUP BY year UNION ALL SELECT id, SUM(quezon),month, year, 'Quezon' description from ptc GROUP BY year UNION ALL SELECT id, SUM(quirino),month, year, 'Quirino' description from ptc GROUP BY year UNION ALL SELECT id, SUM(rizal),month, year, 'Rizal' description from ptc GROUP BY year UNION ALL SELECT id, SUM(romblon),month, year, 'Romblon' description from ptc GROUP BY year UNION ALL SELECT id, SUM(samar),month, year, 'Samar' description from ptc GROUP BY year UNION ALL SELECT id, SUM(sarangani),month, year, 'Sarangani' description from ptc GROUP BY year UNION ALL SELECT id, SUM(siquijor),month, year, 'Siquijor' description from ptc GROUP BY year UNION ALL SELECT id, SUM(sorsogon),month, year, 'Sorsogon' description from ptc GROUP BY year UNION ALL SELECT id, SUM(cotabatoSouth),month, year, 'South Cotabato' description from ptc GROUP BY year UNION ALL SELECT id, SUM(leyteSouth),month, year, 'Southern Leyte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(sultanKudarat),month, year, 'Sultan Kudarat' description from ptc GROUP BY year UNION ALL SELECT id, SUM(sulu),month, year, 'Sulu' description from ptc GROUP BY year UNION ALL SELECT id, SUM(surigaoNorte),month, year, 'Surigao Del Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(surigaoSur),month, year, 'Surigao Del Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(tarlac),month, year, 'Tarlac' description from ptc GROUP BY year UNION ALL SELECT id, SUM(tawitawi),month, year, 'Tawi-tawi' description from ptc GROUP BY year UNION ALL SELECT id, SUM(zambales),month, year, 'Zambales' description from ptc GROUP BY year UNION ALL SELECT id, SUM(zamboangaNorte),month, year, 'Zamboanga Del Norte' description from ptc GROUP BY year UNION ALL SELECT id, SUM(zamboangaSibugay),month, year, 'Zamboanga Sibugay' description from ptc GROUP BY year UNION ALL SELECT id, SUM(zamboangaSur),month, year, 'Zamboanga Del Sur' description from ptc GROUP BY year UNION ALL SELECT id, SUM(international),month, year, 'International' description from ptc GROUP BY year UNION ALL SELECT id, SUM(undetermined),month, year, 'Undetermined' description from ptc GROUP BY year) as ha
    GROUP BY month, year
    ORDER BY month, year """):
        total_location.append(total_year.total)
        year_location.append(total_year.year)

    for ptc_data in ptc.objects.raw(""" SELECT id, year, CONVERT(SUM(sms), UNSIGNED) as sms, CONVERT(SUM(smsWD)/12, UNSIGNED) as smsWD, CONVERT(SUM(smsWE)/12, UNSIGNED) as smsWE, SUM(dwntimeH) as dwmtimeHW, CONVERT(SUM(texterOH), UNSIGNED) as texterOH, CONVERT(SUM(texterNOH), UNSIGNED) as texterNOH, CONVERT(SUM(texterWD), UNSIGNED) as texterWD, CONVERT(SUM(texterWE), UNSIGNED) as texterWE, CONVERT(SUM(keywords), UNSIGNED) as keywords, CONVERT(SUM(male), UNSIGNED) as male, CONVERT(SUM(female),UNSIGNED) as female, SUM(seedAvail) as seedAvail, SUM(seedVar) as seedVar, SUM(landPrep) as landPrep, SUM(cropEsta) as cropEsta, SUM(nutriMng) as nutriMng, SUM(waterMng) as waterMng, SUM(pestMng) as pestMng, SUM(harvMng) as harvMng, SUM(genInfo) as genInfo, SUM(knowProd) as knowProd, SUM(machine) as machine, SUM(foodSci) as foodSci, SUM(training) as training, SUM(palayamanan) as palayamanan, SUM(philrice) as philrice, SUM(otherAgency) as otherAgency, SUM(greetings) as greetings, SUM(thanks) as thanks, SUM(registration) as registration, SUM(others) as others, SUM(rcef) as rcef, SUM(rcefSeed) as rcefSeed, SUM(rcefComp) as rcefComp, SUM(rcefExt) as rcefExt, SUM(rsbsa) as rsbsa, SUM(website) as website, SUM(OH1to5) as OH1to5, SUM(OH6to10) as OH6to10, SUM(OH11to15) as OH11to15, SUM(OH16to20) as OH16to20, SUM(OH21to25) as OH21to25, SUM(OH26to30) as OH26to30, SUM(OH31to1h) as OH31to1h, SUM(OH1hto2h) as OH1hto2h, SUM(OH2hto4h) as OH2hto4h, SUM(OH4hto8h) as OH4hto8h, SUM(OH8hto12h) as OH8hto12h, SUM(OH12hto24h) as OH12hto24h, SUM(OH24to48h) as OH24to48h, SUM(OH48hplus) as OH48hplus, SUM(notRes) as notRes, SUM(NOH1to5) as NOH1to5, SUM(NOH6to10) as NOH6to10, SUM(NOH11to15) as NOH11to15, SUM(NOH16to20) as NOH16to20, SUM(NOH21to25) as NOH21to25, SUM(NOH26to30) as NOH26to30, SUM(NOH31to1h) as NOH31to1h, SUM(NOH1hto2h) as NOH1hto2h, SUM(NOH2hto4h) as NOH2hto4h, SUM(NOH4hto8h) as NOH4hto8h, SUM(NOH8hto12h) as NOH8hto12h, SUM(NOH12hto24h) as NOH12hto24h, SUM(NOH24to48h) as NOH24to48h, SUM(NOH48hplus) as NOH48hplus, SUM(NnotRes) as NnotRes, SUM(WOH1to5) as WOH1to5, SUM(WOH6to10) as WOH6to10, SUM(WOH11to15) as WOH11to15, SUM(WOH16to20) as WOH16to20, SUM(WOH21to25) as WOH21to25, SUM(WOH26to30) as WOH26to30, SUM(WOH31to1h) as WOH31to1h, SUM(WOH1hto2h) as WOH1hto2h, SUM(WOH2hto4h) as WOH2hto4h, SUM(WOH4hto8h) as WOH4hto8h, SUM(WOH8hto12h) as WOH8hto12h, SUM(WOH12hto24h) as WOH12hto24h, SUM(WOH24to48h) as WOH24to48h, SUM(WOH48hplus) as WOH48hplus, SUM(WnotRes) as WnotRes, SUM(abra) as abra, SUM(agusanNorte) as agusanNorte, SUM(agusanSur) as agusanSur, SUM(aklan) as aklan, SUM(albay) as albay, SUM(antique) as antique, SUM(apayao) as apayao, SUM(aurora) as aurora, SUM(basilan) as basilan, SUM(bataan) as bataan, SUM(batanes) as batanes, SUM(batangas) as batangas, SUM(benguet) as benguet, SUM(biliran) as biliran, SUM(bohol) as bohol, SUM(bukidnon) as bukidnon, SUM(bulacan) as bulacan, SUM(cagayan) as cagayan, SUM(camarinesNorte) as camarinesNorte, SUM(camarinesSur) as camarinesSur, SUM(camiguin) as camiguin, SUM(capiz) as capiz, SUM(catanduanes) as catanduanes, SUM(cavite) as cavite, SUM(cebu) as cebu, SUM(compostela) as compostela, SUM(davaoNorte) as davaoNorte, sum(davaoSur) as davaoSur, SUM(davaoOriental) as davaoOriental, SUM(samarEast) as samarEast, SUM(guimaras) as guimaras, SUM(ifugao) as ifugao, SUM(ilocosNorte) as ilocosNorte, SUM(ilocosSur) as ilocosSur, SUM(iloilo) as iloilo, SUM(isabela) as isabela, SUM(kalinga) as kalinga, SUM(launion) as launion, SUM(laguna) as laguna, SUM(lanaoNorte) as lanaoNorte, SUM(lanaoSur) as lanaoSur, SUM(leyte) as leyte, SUM(maguindanao) as maguindanao, SUM(marinduque) as marinduque, SUM(masbate) as masbate, SUM(manila) as manila, SUM(misamisOccidental) as misamisOccidental, SUM(misamisOriental) as misamisOriental, SUM(palawan) as palawan, SUM(pampanga) as pampanga, SUM(pangasinan) as pangasinan, SUM(quezon) as quezon, SUM(quirino) as quirino, SUM(rizal) as rizal, SUM(romblon) as romblon, SUM(samar) as samar, SUM(sarangani) as sarangani, SUM(siquijor) as siquijor, SUM(sorsogon) as sorsogon, SUM(cotabatoSouth) as cotabatoSouth, SUM(leyteSouth) as leyteSouth, SUM(sultanKudarat) as sultanKudarat, SUM(sulu) as sulu, SUM(surigaoNorte) as surigaoNorte, SUM(surigaoSur) as surigaoSur, SUM(tarlac) as tarlac, SUM(tawitawi) as tawitawi, SUM(zambales) as zambales, SUM(zamboangaNorte) as zamboangaNorte, SUM(zamboangaSibugay) as zamboangaSibugay, SUM(zamboangaSur) as zamboangaSur, SUM(international) as international, SUM(undetermined) as undetermined FROM ptc GROUP BY year """):
        id.append(ptc_data.id)
        ptc_year.append(ptc_data.year)
        sms.append(ptc_data.sms)
        smsWD.append(ptc_data.smsWD)
        smsWE.append(ptc_data.smsWE)
        texterOH.append(ptc_data.texterOH)
        texterNOH.append(ptc_data.texterNOH)
        texterWD.append(ptc_data.texterWD)
        texterWE.append(ptc_data.texterWE)
        keywords.append(ptc_data.keywords)
        male.append(ptc_data.male)
        female.append(ptc_data.female)

    for OH_data in ptc.objects.raw(""" SELECT id, CONVERT(SUM(total),UNSIGNED) as OH1to15, CONVERT(SUM(total2),UNSIGNED) as OH16to1h, CONVERT(SUM(total3),UNSIGNED) as OH1hto4h, CONVERT(SUM(total4),UNSIGNED) as OH4hto12h, CONVERT(SUM(total5),UNSIGNED) as OH12up, year FROM(
	SELECT id, CONVERT(SUM(OH1to5), UNSIGNED) as total, CONVERT(SUM(OH16to20), UNSIGNED) as total2, CONVERT(SUM(OH1hto2h),UNSIGNED) as total3, CONVERT(SUM(OH4hto8h), UNSIGNED) as total4, CONVERT(SUM(OH12hto24h), UNSIGNED) as total5, year FROM ptc GROUP BY year UNION ALL
	SELECT id, CONVERT(SUM(OH6to10), UNSIGNED) as total, CONVERT(SUM(OH21to25), UNSIGNED) as total2, CONVERT(SUM(OH2hto4h),UNSIGNED) as total3, CONVERT(SUM(OH8hto12h),UNSIGNED) as total4, CONVERT(SUM(OH24to48h), UNSIGNED) as total5, year FROM ptc GROUP BY year UNION ALL
	SELECT id, CONVERT(SUM(OH11to15), UNSIGNED) as total, CONVERT(SUM(OH26to30), UNSIGNED) as total2, '0' total3, '0' total4, CONVERT(SUM(OH48hplus),UNSIGNED) as total5, year FROM ptc GROUP BY year UNION ALL
	SELECT id, '0' total1, CONVERT(SUM(OH31to1h), UNSIGNED) as total2, '0' total3, '0' total4, '0' total5, year FROM ptc GROUP BY year
    ) as t GROUP BY year """):
        OH1to15.append(OH_data.OH1to15)
        OH16to1h.append(OH_data.OH16to1h)
        OH1hto4h.append(OH_data.OH1hto4h)
        OH4hto12h.append(OH_data.OH4hto12h)
        OH12up.append(OH_data.OH12up)
        OHyear.append(OH_data.year)

    for NOH_data in ptc.objects.raw(""" SELECT id, CONVERT(SUM(total),UNSIGNED) as NOH1to15, CONVERT(SUM(total2),UNSIGNED) as NOH16to1h, CONVERT(SUM(total3),UNSIGNED) as NOH1hto4h, CONVERT(SUM(total4),UNSIGNED) as NOH4hto12h, CONVERT(SUM(total5),UNSIGNED) as NOH12up, year FROM(
	SELECT id, CONVERT(SUM(NOH1to5), UNSIGNED) as total, CONVERT(SUM(NOH16to20), UNSIGNED) as total2, CONVERT(SUM(NOH1hto2h),UNSIGNED) as total3, CONVERT(SUM(NOH4hto8h), UNSIGNED) as total4, CONVERT(SUM(NOH12hto24h), UNSIGNED) as total5, year FROM ptc GROUP BY year UNION ALL
	SELECT id, CONVERT(SUM(NOH6to10), UNSIGNED) as total, CONVERT(SUM(NOH21to25), UNSIGNED) as total2, CONVERT(SUM(NOH2hto4h),UNSIGNED) as total3, CONVERT(SUM(NOH8hto12h),UNSIGNED) as total4, CONVERT(SUM(NOH24to48h), UNSIGNED) as total5, year FROM ptc GROUP BY year UNION ALL
	SELECT id, CONVERT(SUM(NOH11to15), UNSIGNED) as total, CONVERT(SUM(NOH26to30), UNSIGNED) as total2, '0' total3, '0' total4, CONVERT(SUM(NOH48hplus),UNSIGNED) as total5, year FROM ptc GROUP BY year UNION ALL
	SELECT id, '0' total1, CONVERT(SUM(NOH31to1h), UNSIGNED) as total2, '0' total3, '0' total4, '0' total5, year FROM ptc GROUP BY year
    ) as t GROUP BY year """):
        NOH1to15.append(NOH_data.NOH1to15)
        NOH16to1h.append(NOH_data.NOH16to1h)
        NOH1hto4h.append(NOH_data.NOH1hto4h)
        NOH4hto12h.append(NOH_data.NOH4hto12h)
        NOH12up.append(NOH_data.NOH12up)
        NOHyear.append(NOH_data.year)

    for WOH_data in ptc.objects.raw(""" SELECT id, CONVERT(SUM(total),UNSIGNED) as WOH1to15, CONVERT(SUM(total2),UNSIGNED) as WOH16to1h, CONVERT(SUM(total3),UNSIGNED) as WOH1hto4h, CONVERT(SUM(total4),UNSIGNED) as WOH4hto12h, CONVERT(SUM(total5),UNSIGNED) as WOH12up, year FROM(
	SELECT id, CONVERT(SUM(WOH1to5), UNSIGNED) as total, CONVERT(SUM(WOH16to20), UNSIGNED) as total2, CONVERT(SUM(WOH1hto2h),UNSIGNED) as total3, CONVERT(SUM(WOH4hto8h), UNSIGNED) as total4, CONVERT(SUM(WOH12hto24h), UNSIGNED) as total5, year FROM ptc GROUP BY year UNION ALL
	SELECT id, CONVERT(SUM(WOH6to10), UNSIGNED) as total, CONVERT(SUM(WOH21to25), UNSIGNED) as total2, CONVERT(SUM(WOH2hto4h),UNSIGNED) as total3, CONVERT(SUM(WOH8hto12h),UNSIGNED) as total4, CONVERT(SUM(WOH24to48h), UNSIGNED) as total5, year FROM ptc GROUP BY year UNION ALL
	SELECT id, CONVERT(SUM(WOH11to15), UNSIGNED) as total, CONVERT(SUM(WOH26to30), UNSIGNED) as total2, '0' total3, '0' total4, CONVERT(SUM(WOH48hplus),UNSIGNED) as total5, year FROM ptc GROUP BY year UNION ALL
	SELECT id, '0' total1, CONVERT(SUM(WOH31to1h), UNSIGNED) as total2, '0' total3, '0' total4, '0' total5, year FROM ptc GROUP BY year
    ) as t GROUP BY year """):
        WOH1to15.append(WOH_data.WOH1to15)
        WOH16to1h.append(WOH_data.WOH16to1h)
        WOH1hto4h.append(WOH_data.WOH1hto4h)
        WOH4hto12h.append(WOH_data.WOH4hto12h)
        WOH12up.append(WOH_data.WOH12up)
        WOHyear.append(WOH_data.year)

    context = {
    'ptcs':ptcs,
    'location':location,
    'sms_yr':sms_yr,

    'yr2017_data':yr2017_data,
    'yr2018_data':yr2018_data,
    'yr2019_data':yr2019_data,
    'yr2020_data':yr2020_data,
    'yr2021_data':yr2021_data,

    'total_location':total_location,
    'year_location': year_location,
    'ptc_year':ptc_year,
    'sms':sms,
    'smsWD':smsWD,
    'smsWE':smsWE,
    'texterOH':texterOH,
    'texterNOH':texterNOH,
    'texterWD':texterWD,
    'texterWE':texterWE,
    'keywords':keywords,
    'male':male,
    'female':female,

    'OH1to15':OH1to15,
    'OH16to1h':OH16to1h,
    'OH1hto4h':OH1hto4h,
    'OH4hto12h':OH4hto12h,
    'OH12up':OH12up,
    'OHyear':OHyear,

    'NOH1to15':NOH1to15,
    'NOH16to1h':NOH16to1h,
    'NOH1hto4h':NOH1hto4h,
    'NOH4hto12h':NOH4hto12h,
    'NOH12up':NOH12up,
    'NOHyear':NOHyear,

    'WOH1to15':WOH1to15,
    'WOH16to1h':WOH16to1h,
    'WOH1hto4h':WOH1hto4h,
    'WOH4hto12h':WOH4hto12h,
    'WOH12up':WOH12up,
    'WOHyear':WOHyear,
    }
    return render(request,'dashboard/ptc.html',context)

def ptcs_edit(request, pk):
    text = ptc.objects.get(pk=pk)
    ptc_form = ptc_Form(instance=text)
    if request.method == 'POST':
        ptc_form = ptc_Form(request.POST, instance=text)
        if ptc_form.is_valid():
            ptc_form.save()
            return redirect('/ptc')
    context = {'ptc_form':ptc_form}
    return render(request,'dashboard/data_input_ptc.html', context)
def ptcs_delete(request, pk):
    data = ptc.objects.get(pk=pk)
    url = "/ptc_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/ptc')
    context = { 'url': url }
    return render(request, 'dashboard/delete.html', context)

#end PhilRice Text Center
#PhilRice Website
def data_input_pw(request):
    input_menu_toggle = 'active'
    pw_input = 'active'
    pw_form = pw_Form()
    if request.method == 'POST':
        pw_form = pw_Form(request.POST)
        if pw_form.is_valid():
            pw_form.save()
            return redirect('/data_input_pw')

    context = {'pw_form': pw_form,
                'pw_input':pw_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request, 'dashboard/data_input_pw.html', context) #PhilRice website
def pws(request):
    reportndata = 'active'
    pw_table = 'active'
    text = pw.objects.all().exclude(title="-", topic="-")
    context = {'text':text,
    'reportndata':reportndata,
    'pw_table':pw_table}
    return render(request, 'dashboard/pw_data.html', context)
def pws_edit(request, pk):
    text = pw.objects.get(pk=pk)
    pw_form = pw_Form(instance=text)
    if request.method == 'POST':
        pw_form = pw_Form(request.POST, instance=text)
        if pw_form.is_valid():
            pw_form.save()
            return redirect('/pw')
    context = {'pw_form':pw_form}
    return render(request, 'dashboard/data_input_pw.html', context)
def pws_delete(request, pk):
    data = pw.objects.get(pk=pk)
    url = "/pw_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/pw')
    context = { 'url': url}
    return render(request, 'dashboard/delete.html', context)
def data_input_pw_visitor(request):
    input_menu_toggle = 'active'
    pw_input = 'active'
    pw_visitor_form = pw_visitor_Form()
    if request.method == 'POST':
        pw_visitor_form = pw_visitor_Form(request.POST)
        if pw_visitor_form.is_valid():
            pw_visitor_form.save()
            return redirect('/data_input_pw_visitor')

    context = {'pw_visitor_form': pw_visitor_form,
                'pw_input':pw_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request, 'dashboard/data_input_pw_visitor.html', context)
def pws_visitor(request):
    reportndata = 'active'
    pw_table = 'active'
    text = pw_visitor.objects.all()
    context = {'text':text,
    'reportndata':reportndata,
    'pw_table':pw_table}
    return render(request, 'dashboard/pw_visitor_data.html', context)
def pws_visitor_edit(request, pk):
    text = pw_visitor.objects.get(pk=pk)
    pw_visitor_form = pw_visitor_Form(instance=text)
    if request.method == 'POST':
        pw_visitor_form = pw_visitor_Form(request.POST, instance=text)
        if pw_visitor_form.is_valid():
            pw_visitor_form.save()
            return redirect('/pw_visitor')
    context = {'pw_visitor_form': pw_visitor_form}
    return render(request, 'dashboard/data_input_pw_visitor.html', context)
def pws_visitor_delete(request, pk):
    data = pw_visitor.objects.get(pk=pk)
    url = "/pw_visitor_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/pw_visitor')
    context = { 'url': url}
    return render(request, 'dashboard/delete.html', context)

def philricewebsite(request):
    pws = 'active'
    label = []
    fascinated = []
    amused = []
    excited = []
    angry = []
    sad = []
    bored = []

    news = []
    photonews = []
    feature = []

    stories_trend_2017=[]
    stories_trend_2018=[]
    stories_trend_2019=[]
    stories_trend_2020=[]
    stories_trend_2021=[]

    for data in pw.objects.raw('SELECT id, CONVERT(SUM(fascinated),UNSIGNED) as fascinated, CONVERT(SUM(amused),UNSIGNED) as amused, CONVERT(SUM(excited),UNSIGNED) as excited, CONVERT(SUM(angry),UNSIGNED) as angry, CONVERT(SUM(sad),UNSIGNED) as sad, CONVERT(SUM(bored),UNSIGNED) as bored, CONCAT(month, "/", year ) as monthyear FROM pw GROUP BY month, year ORDER BY year, month'):
        label.append(data.monthyear)
        fascinated.append(data.fascinated)
        amused.append(data.amused)
        excited.append(data.excited)
        angry.append(data.angry)
        sad.append(data.sad)
        bored.append(data.bored)

    for data in pw.objects.raw('SELECT id, COUNT(topic) as news FROM pw WHERE classification = "news" GROUP BY month, year ORDER BY year, month'):
        news.append(data.news)

    for data in pw.objects.raw('SELECT id, COUNT(topic) as photonews FROM pw WHERE classification = "photonews" GROUP BY month, year ORDER BY year, month'):
        photonews.append(data.photonews)

    for data in pw.objects.raw('SELECT id, COUNT(topic) as feature FROM pw WHERE classification = "features" GROUP BY month, year ORDER BY year, month'):
        feature.append(data.feature)

    pw_data_features = pw.objects.raw('SELECT id, title, topic, fascinated, amused, excited, angry, sad, bored, date FROM pw WHERE classification="features" ORDER BY date')
    pw_data_news = pw.objects.raw('SELECT id, title, topic, fascinated, amused, excited, angry, sad, bored, date FROM pw WHERE classification="news" ORDER BY date')
    pw_data_photonews = pw.objects.raw('SELECT id, title, topic, fascinated, amused, excited, angry, sad, bored, date FROM pw WHERE classification="photonews" ORDER BY date')


    for data in pw.objects.raw(""" SELECT id, CONVERT(COUNT(topic) - 1,UNSIGNED) as stories, month, year FROM `pw` WHERE year='2017' GROUP BY month """):
        stories_trend_2017.append(data.stories)
    for data in pw.objects.raw(""" SELECT id, CONVERT(COUNT(topic) - 1,UNSIGNED) as stories, month, year FROM `pw` WHERE year='2018' GROUP BY month """):
        stories_trend_2018.append(data.stories)
    for data in pw.objects.raw(""" SELECT id, CONVERT(COUNT(topic) - 1,UNSIGNED) as stories, month, year FROM `pw` WHERE year='2019' GROUP BY month """):
        stories_trend_2019.append(data.stories)
    for data in pw.objects.raw(""" SELECT id, CONVERT(COUNT(topic) - 1,UNSIGNED) as stories, month, year FROM `pw` WHERE year='2020' GROUP BY month """):
        stories_trend_2020.append(data.stories)
    for data in pw.objects.raw(""" SELECT id, CONVERT(COUNT(topic) - 1,UNSIGNED) as stories, month, year FROM `pw` WHERE year='2021' GROUP BY month """):
        stories_trend_2021.append(data.stories)

    context = {
    'pws':pws,
    'label': label,
    'fascinated': fascinated,
    'amused': amused,
    'excited': excited,
    'angry': angry,
    'sad': sad,
    'bored': bored,
    'news': news,
    'photonews': photonews,
    'feature': feature,
    'pw_data_features': pw_data_features,
    'pw_data_news':pw_data_news,
    'pw_data_photonews':pw_data_photonews,

    'stories_trend_2017':stories_trend_2017,
    'stories_trend_2018':stories_trend_2018,
    'stories_trend_2019':stories_trend_2019,
    'stories_trend_2020':stories_trend_2020,
    'stories_trend_2021':stories_trend_2021,
    }
    return render(request, 'dashboard/pw.html', context)
def philricewebsite_visitor(request):
    pws = 'active'
    label = []
    visit = []
    pageviews = []
    male = []
    female = []
    nosex = []
    syes = []
    sno = []
    organic = []
    direct = []
    social = []
    referral = []
    mobile = []
    desktop = []
    tablet = []

    visit_trend_2017 = []
    pageviews_trend_2017 = []
    visit_trend_2018 = []
    pageviews_trend_2018 = []
    visit_trend_2019 = []
    pageviews_trend_2019 = []
    visit_trend_2020 = []
    pageviews_trend_2020 = []
    visit_trend_2021 = []
    pageviews_trend_2021 = []

    for data in pw_visitor.objects.raw("""SELECT id, CONVERT(SUM(visit),UNSIGNED) AS visit, CONVERT(SUM(pageviews), UNSIGNED) AS pageviews, CONVERT(SUM(male),UNSIGNED) AS male, CONVERT(SUM(female),UNSIGNED) AS female, CONVERT(SUM(nosex),UNSIGNED) AS nosex, CONVERT(SUM(syes),UNSIGNED) AS syes, CONVERT(SUM(sno),UNSIGNED) AS sno, CONVERT(SUM(organic),UNSIGNED) AS organic, CONVERT(SUM(direct),UNSIGNED) AS direct, CONVERT(SUM(social),UNSIGNED) AS social, CONVERT(SUM(referral), UNSIGNED) AS referral, CONVERT(SUM(mobile),UNSIGNED) AS mobile, CONVERT(SUM(desktop),UNSIGNED) as desktop, CONVERT(SUM(tablet),UNSIGNED) AS tablet, year FROM pw_visitor GROUP BY year"""):
        label.append(data.year)
        visit.append(data.visit)
        pageviews.append(data.pageviews)
        male.append(data.male)
        female.append(data.female)
        nosex.append(data.nosex)
        syes.append(data.syes)
        sno.append(data.sno)
        organic.append(data.organic)
        direct.append(data.direct)
        social.append(data.social)
        referral.append(data.referral)
        mobile.append(data.mobile)
        desktop.append(data.desktop)
        tablet.append(data.tablet)

    location = pw_visitor.objects.raw(""" SELECT id, location1 as location, CONVERT(SUM(nlocation1),UNSIGNED) as total, month, year FROM pw_visitor WHERE nlocation1!="0" GROUP BY year,month UNION ALL SELECT id, location2, CONVERT(SUM(nlocation2),UNSIGNED), month, year FROM pw_visitor WHERE nlocation2!="0" GROUP BY year,month UNION ALL SELECT id, location3, CONVERT(SUM(nlocation3),UNSIGNED), month, year FROM pw_visitor WHERE nlocation3!="0" GROUP BY year,month UNION ALL SELECT id, location4, CONVERT(SUM(nlocation4),UNSIGNED), month, year FROM pw_visitor WHERE nlocation4!="0" GROUP BY year,month UNION ALL SELECT id, location5, CONVERT(SUM(nlocation5),UNSIGNED), month, year FROM pw_visitor WHERE nlocation5!="0" GROUP BY year,month ORDER BY month,year """)

    # update yearly
    for data in pw_visitor.objects.raw(""" SELECT id, CONVERT(SUM(visit),UNSIGNED) as visit, CONVERT(SUM(pageviews),UNSIGNED) as pageviews, month, year FROM `pw_visitor` WHERE year='2017' GROUP BY month """):
        visit_trend_2017.append(data.visit)
        pageviews_trend_2017.append(data.pageviews)
    for data in pw_visitor.objects.raw(""" SELECT id, CONVERT(SUM(visit),UNSIGNED) as visit, CONVERT(SUM(pageviews),UNSIGNED) as pageviews, month, year FROM `pw_visitor` WHERE year='2018' GROUP BY month """):
        visit_trend_2018.append(data.visit)
        pageviews_trend_2018.append(data.pageviews)
    for data in pw_visitor.objects.raw(""" SELECT id, CONVERT(SUM(visit),UNSIGNED) as visit, CONVERT(SUM(pageviews),UNSIGNED) as pageviews, month, year FROM `pw_visitor` WHERE year='2019' GROUP BY month """):
        visit_trend_2019.append(data.visit)
        pageviews_trend_2019.append(data.pageviews)
    for data in pw_visitor.objects.raw(""" SELECT id, CONVERT(SUM(visit),UNSIGNED) as visit, CONVERT(SUM(pageviews),UNSIGNED) as pageviews, month, year FROM `pw_visitor` WHERE year='2020' GROUP BY month """):
        visit_trend_2020.append(data.visit)
        pageviews_trend_2020.append(data.pageviews)
    for data in pw_visitor.objects.raw(""" SELECT id, CONVERT(SUM(visit),UNSIGNED) as visit, CONVERT(SUM(pageviews),UNSIGNED) as pageviews, month, year FROM `pw_visitor` WHERE year='2021' GROUP BY month """):
        visit_trend_2021.append(data.visit)
        pageviews_trend_2021.append(data.pageviews)
    # update yearly end


    context = {
        'pws':pws,
        'label': label,
        'visit': visit,
        'pageviews': pageviews,
        'male': male,
        'female': female,
        'nosex':nosex,
        'syes': syes,
        'sno': sno,
        'organic': organic,
        'direct': direct,
        'social':social,
        'referral':referral,
        'mobile':mobile,
        'desktop':desktop,
        'tablet':tablet,
        'location':location,

        'visit_trend_2017':visit_trend_2017,
        'pageviews_trend_2017':pageviews_trend_2017,
        'visit_trend_2018':visit_trend_2018,
        'pageviews_trend_2018':pageviews_trend_2018,
        'visit_trend_2019':visit_trend_2019,
        'pageviews_trend_2019':pageviews_trend_2019,
        'visit_trend_2020':visit_trend_2020,
        'pageviews_trend_2020':pageviews_trend_2020,
        'visit_trend_2021':visit_trend_2021,
        'pageviews_trend_2021':pageviews_trend_2021,
    }
    return render(request, 'dashboard/pw_visitor.html', context)
#end PhilRice Website
#PinoyRice
    #visitor
def data_input_pr_visitor(request):
    input_menu_toggle = 'active'
    pr_input = 'active'
    pr_visitor_form = pr_visitor_Form()
    if request.method == 'POST':
        pr_visitor_form = pr_visitor_Form(request.POST)
        if pr_visitor_form.is_valid():
            pr_visitor_form.save()
            return redirect('/data_input_pr_visitor')

    context = {'pr_visitor_form': pr_visitor_form,
                'pr_input':pr_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request, 'dashboard/data_input_pr_visitor.html', context)#Pinoy Rice
def prs_visitor(request):
    reportndata = 'active'
    pr_table = 'active'
    text = pr_visitor.objects.all()
    context = {'text':text,
    'reportndata':reportndata,
    'pr_table':pr_table
    }
    return render(request,'dashboard/pr_data.html', context)
def prs_visitor_edit(request, pk):
    text = pr_visitor.objects.get(pk=pk)
    pr_visitor_form = pr_visitor_Form(instance=text)
    if request.method == 'POST':
        pr_visitor_form = pr_visitor_Form(request.POST, instance=text)
        if pr_visitor_form.is_valid():
            pr_visitor_form.save()
            return redirect('/pr_visitor')
    context = {'pr_visitor_form':pr_visitor_form}
    return render(request, 'dashboard/data_input_pr_visitor.html', context)
def prs_visitor_delete(request, pk):
    data = pr_visitor.objects.get(pk=pk)
    url = "/pr_visitor_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/pr_visitor')
    context = { 'url': url }
    return render(request, 'dashboard/delete.html', context)
    #end visitor
def data_input_pr_upload(request):
    input_menu_toggle = 'active'
    pr_input = 'active'
    pr_upload_form = pr_upload_Form()
    if request.method == 'POST':
        pr_upload_form = pr_upload_Form(request.POST)
        if pr_upload_form.is_valid():
            pr_upload_form.save()
            return redirect('/data_input_pr_upload')

    context = {'pr_upload_form':pr_upload_form,
                'pr_input':pr_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request,'dashboard/data_input_pr_upload.html', context)
def prs_upload(request):
    reportndata = 'active'
    pr_table = 'active'
    text = pr_upload.objects.all().exclude(title="-",topic="-")
    context = {'text':text,
    'reportndata':reportndata,
    'pr_table':pr_table}
    return render(request, 'dashboard/pr_upload_data.html', context)
def prs_upload_edit(request, pk):
    text = pr_upload.objects.get(pk=pk)
    pr_upload_form = pr_upload_Form(instance=text)
    if request.method == 'POST':
        pr_upload_form = pr_upload_Form(request.POST, instance=text)
        if pr_upload_form.is_valid():
            pr_upload_form.save()
            return redirect('/pr_upload')
    context = {'pr_upload_form':pr_upload_form}
    return render(request, 'dashboard/data_input_pr_upload.html', context)
def prs_upload_delete(request, pk):
    data = pr_upload.objects.get(pk=pk)
    url = "/pr_upload_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/pr_upload')
    context = { 'url': url }
    return render(request, 'dashboard/delete.html',context)

def pinoyrice_visitor(request):
    pr = 'active'
    label = []
    visit = []
    download = []
    pageviews = []
    male = []
    female = []
    nosex = []
    age18to24 = []
    age25to34 = []
    age35to44 = []
    age45to54 = []
    age55to64 = []
    age65above = []
    noage=[]
    syes = []
    sno = []
    mobile = []
    desktop = []
    tablet = []
    organic = []
    direct = []
    social = []
    referral = []

    visit_trend_2017 = []
    download_trend_2017 = []
    pageviews_trend_2017 = []
    visit_trend_2018 = []
    download_trend_2018 = []
    pageviews_trend_2018 = []
    visit_trend_2019 = []
    download_trend_2019 = []
    pageviews_trend_2019 = []
    visit_trend_2020 = []
    download_trend_2020 = []
    pageviews_trend_2020 = []
    visit_trend_2021 = []
    download_trend_2021 = []
    pageviews_trend_2021 = []


    for data in pr_visitor.objects.raw("""SELECT id, CONVERT(SUM(visit),UNSIGNED) as visit, CONVERT(SUM(download),UNSIGNED) as download, CONVERT(SUM(pageviews),UNSIGNED) as pageviews, CONVERT(SUM(male),UNSIGNED) as male, CONVERT(SUM(female),UNSIGNED) as female, CONVERT(SUM(nosex),UNSIGNED)as nosex, CONVERT(SUM(age18to24),UNSIGNED) as age18to24, CONVERT(SUM(age25to34),UNSIGNED) as age25to34, CONVERT(SUM(age35to44),UNSIGNED) as age35to44, CONVERT(SUM(age45to54),UNSIGNED) as age45to54, CONVERT(SUM(age55to64),UNSIGNED) as age55to64, CONVERT(SUM(age65above),UNSIGNED) as age65above, CONVERT(SUM(noage),UNSIGNED) as noage, CONVERT(SUM(syes),UNSIGNED) as syes, CONVERT(SUM(sno),UNSIGNED) as sno, CONVERT(SUM(mobile),UNSIGNED) as mobile, CONVERT(SUM(desktop),UNSIGNED) as desktop, CONVERT(SUM(tablet),UNSIGNED) as tablet, CONVERT(SUM(organic),UNSIGNED) as organic, CONVERT(SUM(direct),UNSIGNED) as direct, CONVERT(SUM(social),UNSIGNED) as social, CONVERT(SUM(referral),UNSIGNED) as referral, year FROM pr_visitor GROUP BY year"""):
        label.append(data.year)
        visit.append(data.visit)
        download.append(data.download)
        pageviews.append(data.pageviews)
        male.append(data.male)
        female.append(data.female)
        nosex.append(data.nosex)
        age18to24.append(data.age18to24)
        age25to34.append(data.age25to34)
        age35to44.append(data.age35to44)
        age45to54.append(data.age45to54)
        age55to64.append(data.age55to64)
        age65above.append(data.age65above)
        noage.append(data.noage)
        syes.append(data.syes)
        sno.append(data.sno)
        mobile.append(data.mobile)
        desktop.append(data.desktop)
        tablet.append(data.tablet)
        organic.append(data.organic)
        direct.append(data.direct)
        social.append(data.social)
        referral.append(data.referral)

    location = pr_visitor.objects.raw(""" SELECT id, location1 as location, SUM(nlocation1) as count, month, year FROM pr_visitor WHERE nlocation1!="0" GROUP BY month, year UNION ALL SELECT id, location2, SUM(nlocation2) as nlocation2, month, year FROM pr_visitor WHERE nlocation2!="0" GROUP BY month, year UNION ALL SELECT id, location3, SUM(nlocation3) as nlocation3, month, year FROM pr_visitor WHERE nlocation3!="0" GROUP BY month, year UNION ALL SELECT id, location4, SUM(nlocation4) as nlocation4, month, year FROM pr_visitor WHERE nlocation4!="0" GROUP BY month, year UNION ALL SELECT id, location5, SUM(nlocation5) as nlocation5, month, year FROM pr_visitor WHERE nlocation5!="0" GROUP BY month, year UNION ALL SELECT id, location6, SUM(nlocation6) as nlocation6, month, year FROM pr_visitor WHERE nlocation6!="0" GROUP BY month, year UNION ALL SELECT id, location7, SUM(nlocation7) as nlocation7, month, year FROM pr_visitor WHERE nlocation7!="0" GROUP BY month, year UNION ALL SELECT id, location8, SUM(nlocation8) as nlocation8, month, year FROM pr_visitor WHERE nlocation8="0" GROUP BY month, year UNION ALL SELECT id, location9, SUM(nlocation9) as nlocation9, month, year FROM pr_visitor WHERE nlocation9!="0" GROUP BY month, year UNION ALL SELECT id, location10, SUM(nlocation10) as nlocation10, month, year FROM pr_visitor WHERE nlocation10!="0" GROUP BY month, year ORDER BY year, month """)

    # update yearly
    for data in pr_visitor.objects.raw(""" SELECT id, CONVERT(SUM(visit),UNSIGNED) as visit, CONVERT(SUM(download),UNSIGNED) as download, CONVERT(SUM(pageviews), UNSIGNED) as pageviews, month, year FROM `pr_visitor` WHERE year='2017' GROUP BY month """):
        visit_trend_2017.append(data.visit)
        download_trend_2017.append(data.download)
        pageviews_trend_2017.append(data.pageviews)
    for data in pr_visitor.objects.raw(""" SELECT id, CONVERT(SUM(visit),UNSIGNED) as visit, CONVERT(SUM(download),UNSIGNED) as download, CONVERT(SUM(pageviews), UNSIGNED) as pageviews, month, year FROM `pr_visitor` WHERE year='2018' GROUP BY month """):
        visit_trend_2018.append(data.visit)
        download_trend_2018.append(data.download)
        pageviews_trend_2018.append(data.pageviews)
    for data in pr_visitor.objects.raw(""" SELECT id, CONVERT(SUM(visit),UNSIGNED) as visit, CONVERT(SUM(download),UNSIGNED) as download, CONVERT(SUM(pageviews), UNSIGNED) as pageviews, month, year FROM `pr_visitor` WHERE year='2019' GROUP BY month """):
        visit_trend_2019.append(data.visit)
        download_trend_2019.append(data.download)
        pageviews_trend_2019.append(data.pageviews)
    for data in pr_visitor.objects.raw(""" SELECT id, CONVERT(SUM(visit),UNSIGNED) as visit, CONVERT(SUM(download),UNSIGNED) as download, CONVERT(SUM(pageviews), UNSIGNED) as pageviews, month, year FROM `pr_visitor` WHERE year='2020' GROUP BY month """):
        visit_trend_2020.append(data.visit)
        download_trend_2020.append(data.download)
        pageviews_trend_2020.append(data.pageviews)
    for data in pr_visitor.objects.raw(""" SELECT id, CONVERT(SUM(visit),UNSIGNED) as visit, CONVERT(SUM(download),UNSIGNED) as download, CONVERT(SUM(pageviews), UNSIGNED) as pageviews, month, year FROM `pr_visitor` WHERE year='2021' GROUP BY month """):
        visit_trend_2021.append(data.visit)
        download_trend_2021.append(data.download)
        pageviews_trend_2021.append(data.pageviews)

    # update yearly end
    context = {
        'pr':pr,
        'label': label,
        'visit': visit,
        'download': download,
        'pageviews':pageviews,
        'male': male,
        'female': female,
        'nosex':nosex,
        'age18to24': age18to24,
        'age25to34': age25to34,
        'age35to44': age35to44,
        'age45to54': age45to54,
        'age55to64': age55to64,
        'age65above': age65above,
        'noage':noage,
        'syes': syes,
        'sno': sno,
        'mobile':mobile,
        'desktop':desktop,
        'tablet':tablet,
        'organic':organic,
        'direct':direct,
        'social':social,
        'referral':referral,
        'location':location,

        'visit_trend_2017':visit_trend_2017,
        'download_trend_2017':download_trend_2017,
        'pageviews_trend_2017':pageviews_trend_2017,
        'visit_trend_2018':visit_trend_2018,
        'download_trend_2018':download_trend_2018,
        'pageviews_trend_2018':pageviews_trend_2018,
        'visit_trend_2019':visit_trend_2019,
        'download_trend_2019':download_trend_2019,
        'pageviews_trend_2019':pageviews_trend_2019,
        'visit_trend_2020':visit_trend_2020,
        'download_trend_2020':download_trend_2020,
        'pageviews_trend_2020':pageviews_trend_2020,
        'visit_trend_2021':visit_trend_2021,
        'download_trend_2021':download_trend_2021,
        'pageviews_trend_2021':pageviews_trend_2021,
    }
    return render(request, 'dashboard/pr.html',context)
def pinoyrice_upload(request):
    pr = 'active'
    label = []
    title = []

    files_trend_2017 = []
    files_trend_2018 = []
    files_trend_2019 = []
    files_trend_2020 = []
    files_trend_2021 = []

    for data in pr_upload.objects.raw('SELECT id, COUNT(title) as title, year FROM pr_upload GROUP BY month, year ORDER BY year'):
        label.append(data.year)
        title.append(data.title)

    pr_upload_data = pr_upload.objects.raw(""" SELECT id, total, description, month, year FROM ( SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Crop' description, month, year FROM pr_upload WHERE topic="crop" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'General Info' description, month, year FROM pr_upload WHERE topic="general info" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Harvest' description, month, year FROM pr_upload WHERE topic="harvest" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Land' description, month, year FROM pr_upload WHERE topic="land" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Machine' description, month, year FROM pr_upload WHERE topic="machine" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Nutrient' description, month, year FROM pr_upload WHERE topic="nutrient" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Palayamanan' description, month, year FROM pr_upload WHERE topic="palayamanan" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'PalayCheck' description, month, year FROM pr_upload WHERE topic="palaycheck" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Pest' description, month, year FROM pr_upload WHERE topic="pest" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Planting' description, month, year FROM pr_upload WHERE topic="planting" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Post Harvest' description, month, year FROM pr_upload WHERE topic="postharvest" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'RCEF' description, month, year FROM pr_upload WHERE topic="rcef" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Seed' description, month, year FROM pr_upload WHERE topic="seed" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Training' description, month, year FROM pr_upload WHERE topic="training" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Water' description, month, year FROM pr_upload WHERE topic="water" GROUP BY year, month) as t ORDER BY year, month """)

    pr_upload_type = pr_upload.objects.raw(""" SELECT id, total, description, month, year FROM ( SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Accordion' description, month, year FROM pr_upload WHERE type="accordion" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Audio' description, month, year FROM pr_upload WHERE type="audio" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Book' description, month, year FROM pr_upload WHERE type="book" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Booklet' description, month, year FROM pr_upload WHERE type="booklet" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Broadcast Release' description, month, year FROM pr_upload WHERE type="broadcast release" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Data' description, month, year FROM pr_upload WHERE type="data" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Handouts' description, month, year FROM pr_upload WHERE type="handouts" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Infographics' description, month, year FROM pr_upload WHERE type="infographics" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'KSL' description, month, year FROM pr_upload WHERE type="ksl" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Learning Modules' description, month, year FROM pr_upload WHERE type="learning modules" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Magazine' description, month, year FROM pr_upload WHERE type="magazine" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Poster' description, month, year FROM pr_upload WHERE type="poster" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Powerpoint' description, month, year FROM pr_upload WHERE type="powerpoint" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'RS4DM' description, month, year FROM pr_upload WHERE type="rs4dm" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'RTB' description, month, year FROM pr_upload WHERE type="rtb" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Technoguide' description, month, year FROM pr_upload WHERE type="technoguide" GROUP BY year, month
    UNION ALL SELECT id, CONVERT(COUNT(title),UNSIGNED) as total, 'Video' description, month, year FROM pr_upload WHERE type="video" GROUP BY year, month) as t ORDER BY year, month """)


    # update yearly
    for data in pr_upload.objects.raw(""" SELECT id, CONVERT(IF(title!="-",COUNT(title),COUNT(title) - 1),UNSIGNED) as title, month, year FROM `pr_upload` WHERE year='2017' GROUP BY year, month """):
        files_trend_2017.append(data.title)
    for data in pr_upload.objects.raw(""" SELECT id, CONVERT(IF(title!="-",COUNT(title),COUNT(title) - 1),UNSIGNED) as title, month, year FROM `pr_upload` WHERE year='2018' GROUP BY year, month """):
        files_trend_2018.append(data.title)
    for data in pr_upload.objects.raw(""" SELECT id, CONVERT(IF(title!="-",COUNT(title),COUNT(title) - 1),UNSIGNED) as title, month, year FROM `pr_upload` WHERE year='2019' GROUP BY year, month """):
        files_trend_2019.append(data.title)
    for data in pr_upload.objects.raw(""" SELECT id, CONVERT(IF(title!="-",COUNT(title),COUNT(title) - 1),UNSIGNED) as title, month, year FROM `pr_upload` WHERE year='2020' GROUP BY year, month """):
        files_trend_2020.append(data.title)
    for data in pr_upload.objects.raw(""" SELECT id, CONVERT(IF(title!="-",COUNT(title),COUNT(title) - 1),UNSIGNED) as title, month, year FROM `pr_upload` WHERE year='2021' GROUP BY year, month """):
        files_trend_2021.append(data.title)
    # update yearly end

    context = {
    'pr':pr,
    'label' : label,
    'title' : title,
    'pr_upload_data':pr_upload_data,
    'pr_upload_type': pr_upload_type,

    'files_trend_2017':files_trend_2017,
    'files_trend_2018':files_trend_2018,
    'files_trend_2019':files_trend_2019,
    'files_trend_2020':files_trend_2020,
    'files_trend_2021':files_trend_2021,
    }
    return render(request, 'dashboard/pr_upload.html',context)

#end PinoyRice
#radio
def data_input_radio_visitor(request):
    input_menu_toggle = 'active'
    radio_input = 'active'
    radio_visitor_form = radio_visitor_Form()
    if request.method == 'POST':
        radio_visitor_form = radio_visitor_Form(request.POST)
        if radio_visitor_form.is_valid():
            radio_visitor_form.save()
            return redirect('/data_input_radio_visitor')

    context = {'radio_visitor_form': radio_visitor_form,
                'radio_input':radio_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request, 'dashboard/data_input_radio_visitor.html', context)
def radios_visitor(request):
    reportndata = 'active'
    radio_table = 'active'
    text = radio_visitor.objects.all()
    context = {'text':text,
    'reportndata':reportndata,
    'radio_table':radio_table}
    return render(request, 'dashboard/radio_visitor.html', context)
def radios_visitor_edit(request, pk):
    text = radio_visitor.objects.get(pk=pk)
    radio_visitor_form = radio_visitor_Form(instance=text)
    if request.method == 'POST':
        radio_visitor_form = radio_visitor_Form(request.POST, instance=text)
        if radio_visitor_form.is_valid():
            radio_visitor_form.save()
            return redirect('/radio_visitor')
    context = {'radio_visitor_form': radio_visitor_form}
    return render(request, 'dashboard/data_input_radio_visitor.html', context)
def radios_visitor_delete(request, pk):
    data = radio_visitor.objects.get(pk=pk)
    url = "/radio_visitor_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/radio_visitor')
    context = { 'url': url }
    return render(request, 'dashboard/delete.html', context)

def data_input_radio_upload(request):
    input_menu_toggle = 'active'
    radio_input = 'active'
    radio_upload_form = radio_upload_Form()
    if request.method == 'POST':
        radio_upload_form = radio_upload_Form(request.POST)
        if radio_upload_form.is_valid():
            radio_upload_form.save()
            return redirect('/data_input_radio_upload')

    context = {'radio_upload_form': radio_upload_form,
                'radio_input':radio_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request, 'dashboard/data_input_radio_upload.html', context)
def radios_upload(request):
    reportndata = 'active'
    radio_table = 'active'
    text = radio_upload.objects.all()
    context = {'text':text,
    'reportndata':reportndata,
    'radio_table':radio_table}
    return render(request, 'dashboard/radio_upload.html', context)
def radios_upload_edit(request, pk):
    text = radio_upload.objects.get(pk=pk)
    radio_upload_form = radio_upload_Form(instance=text)
    if request.method == 'POST':
        radio_upload_form = radio_upload_Form(request.POST, instance=text)
        if radio_upload_form.is_valid():
            radio_upload_form.save()
            return redirect('/radio_upload')
    context = {'radio_upload_form': radio_upload_form}
    return render(request, 'dashboard/data_input_radio_upload.html', context)
def radios_upload_delete(request, pk):
    data = radio_upload.objects.get(pk=pk)
    url = "/radio_upload_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/radio_upload')
    context = { 'url': url }
    return render(request, 'dashboard/delete.html', context)

def radio(request):
    radio = 'active'
    label = []
    ndetails = []
    male = []
    female = []

    label2 = []
    satisfied = []
    nsatisfied = []

    respondents = []

    segment_trend_2017 = []
    segment_trend_2018 = []
    segment_trend_2019 = []
    segment_trend_2020 = []
    segment_trend_2021 = []

    respondents_trend_2017 = []
    respondents_trend_2018 = []
    respondents_trend_2019 = []
    respondents_trend_2020 = []
    respondents_trend_2021 = []

    for data in radio_visitor.objects.raw('SELECT id, COUNT(topic) as ndetails, year FROM radio_visitor GROUP BY year ORDER BY year'):
        label.append(data.year)
        ndetails.append(data.ndetails)

    for data in radio_visitor.objects.raw('SELECT id, COUNT(sex) as male FROM radio_visitor WHERE sex="male" GROUP BY year ORDER BY year'):
        male.append(data.male)

    for data in radio_visitor.objects.raw('SELECT id, COUNT(sex) as female FROM radio_visitor WHERE sex="female" GROUP BY year ORDER BY year'):
        female.append(data.female)

    for data in radio_upload.objects.raw('SELECT id, CONVERT(SUM(respondents),UNSIGNED) as respondents, year FROM radio_upload GROUP BY year ORDER BY year'):
        label2.append(data.year)
        respondents.append(data.respondents)

    for data in radio_upload.objects.raw('SELECT id, CONVERT(SUM(syes), UNSIGNED) as satisfied, CONVERT(SUM(sno), UNSIGNED) as nsatisfied FROM radio_upload GROUP BY year ORDER BY year'):
        satisfied.append(data.satisfied)
        nsatisfied.append(data.nsatisfied)

    radio_data = radio_visitor.objects.raw('SELECT id, topic, interviewee, sex, station, frequency, location, time, month, day, year FROM radio_visitor WHERE topic!="-" AND title!="-" ORDER BY time DESC, month DESC, day DESC, year DESC')
    # update yearly
    for data in radio_visitor.objects.raw(""" SELECT id, CONVERT(IF(topic!="-",COUNT(topic), COUNT(topic) - 1),UNSIGNED) as segment, month, year FROM `radio_visitor` WHERE year='2017' GROUP BY month """):
        segment_trend_2017.append(data.segment)
    for data in radio_visitor.objects.raw(""" SELECT id, CONVERT(IF(topic!="-",COUNT(topic), COUNT(topic) - 1),UNSIGNED) as segment, month, year FROM `radio_visitor` WHERE year='2018' GROUP BY month """):
        segment_trend_2018.append(data.segment)
    for data in radio_visitor.objects.raw(""" SELECT id, CONVERT(IF(topic!="-",COUNT(topic), COUNT(topic) - 1),UNSIGNED) as segment, month, year FROM `radio_visitor` WHERE year='2019' GROUP BY month """):
        segment_trend_2019.append(data.segment)
    for data in radio_visitor.objects.raw(""" SELECT id, CONVERT(IF(topic!="-",COUNT(topic), COUNT(topic) - 1),UNSIGNED) as segment, month, year FROM `radio_visitor` WHERE year='2020' GROUP BY month """):
        segment_trend_2020.append(data.segment)
    for data in radio_visitor.objects.raw(""" SELECT id, CONVERT(IF(topic!="-",COUNT(topic), COUNT(topic) - 1),UNSIGNED) as segment, month, year FROM `radio_visitor` WHERE year='2021' GROUP BY month """):
        segment_trend_2021.append(data.segment)


    for data in radio_upload.objects.raw(""" SELECT id, CONVERT(SUM(respondents), UNSIGNED) as respondents, month, year FROM `radio_upload` WHERE year='2017' GROUP BY month """):
        respondents_trend_2017.append(data.respondents)
    for data in radio_upload.objects.raw(""" SELECT id, CONVERT(SUM(respondents), UNSIGNED) as respondents, month, year FROM `radio_upload` WHERE year='2018' GROUP BY month """):
        respondents_trend_2018.append(data.respondents)
    for data in radio_upload.objects.raw(""" SELECT id, CONVERT(SUM(respondents), UNSIGNED) as respondents, month, year FROM `radio_upload` WHERE year='2019' GROUP BY month """):
        respondents_trend_2019.append(data.respondents)
    for data in radio_upload.objects.raw(""" SELECT id, CONVERT(SUM(respondents), UNSIGNED) as respondents, month, year FROM `radio_upload` WHERE year='2020' GROUP BY month """):
        respondents_trend_2020.append(data.respondents)
    for data in radio_upload.objects.raw(""" SELECT id, CONVERT(SUM(respondents), UNSIGNED) as respondents, month, year FROM `radio_upload` WHERE year='2021' GROUP BY month """):
        respondents_trend_2021.append(data.respondents)
    # update yearly end
    context = {
    'radio':radio,
    'label': label,
    'ndetails': ndetails,
    'male': male,
    'female': female,
    'label2':label2,
    'satisfied': satisfied,
    'nsatisfied': nsatisfied,
    'radio_data': radio_data,
    'respondents':respondents,

    'segment_trend_2017':segment_trend_2017,
    'segment_trend_2018':segment_trend_2018,
    'segment_trend_2019':segment_trend_2019,
    'segment_trend_2020':segment_trend_2020,
    'segment_trend_2021':segment_trend_2021,

    'respondents_trend_2017':respondents_trend_2017,
    'respondents_trend_2018':respondents_trend_2018,
    'respondents_trend_2019':respondents_trend_2019,
    'respondents_trend_2020':respondents_trend_2020,
    'respondents_trend_2021':respondents_trend_2021,
    }
    return render(request, 'dashboard/radio.html', context)

#end radio
# kp
def data_input_kp(request):
    input_menu_toggle = 'active'
    kp_inputs = 'active'
    kp_input_table = kp_input.objects.exclude(title="-")
    kp_input_form = kp_input_Form()
    if request.method == 'POST':
        kp_input_form = kp_input_Form(request.POST)
        if kp_input_form.is_valid():
            kp_input_id = kp_input_form.save()

            id = kp_input_id.id
            month = kp_input_id.monthfortable
            year= kp_input_id.datefortable
            quantity = 0
            date2 = kp_input_id.date_record

            cursor = connections['default'].cursor()
            cursor.execute("INSERT INTO kp_distribute(`Kp_id`,`Quantity`,`Month`,`Year`) VALUES( %s, %s, %s, %s )", [id, quantity, month, year])
            cursor.execute("INSERT INTO kp_input_stock(`kp_id`,`stocks`,`date_recorded`) VALUES( %s, %s, %s )", [id, quantity, date2])
            return redirect('/data_input_kp')

    context = {'kp_input_form':kp_input_form,
                'kp_inputs':kp_inputs,
                'input_menu_toggle':input_menu_toggle,
                'kp_input_table':kp_input_table}
    return render(request, 'dashboard/data_input_kp.html', context)
def kps_edit(request, pk):
    text = kp_input.objects.get(pk=pk)
    filter_type = text.type
    kp_input_table = kp_input.objects.filter(type=filter_type).exclude(title="-")
    kp_input_form = kp_input_Form(instance=text)
    if request.method == 'POST':
        kp_input_form = kp_input_Form(request.POST, instance=text)
        if kp_input_form.is_valid():
            kp_input_id = kp_input_form.save()
            id = kp_input_id.id
            date = kp_input_id.date_record
            # kp_input_stock.objects.filter(id=id).update(date_recorded=date)
            cursor = connections['default'].cursor()
            cursor.execute(" UPDATE kp_input_stock SET date_recorded = %s WHERE id = %s ", [date, id])
            return redirect('/data_input_kp')

    context = {'kp_input_form':kp_input_form,
               'kp_input_table':kp_input_table}
    return render(request, 'dashboard/data_input_kp.html', context)
def kps_delete(request, pk):
    data = kp_input.objects.get(pk=pk)
    url = "/kp_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/data_input_kp')
    context = { 'url': url}
    return render(request, 'dashboard/delete.html', context)

def data_input_kp_stock(request):
    input_menu_toggle = 'active'
    kp_inputs = 'active'
    kp_stock = kp_input_stock.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press, kp_input_stock.date_recorded FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    kp_input_stock_form = kp_input_stock_Form()

    if request.method == 'POST':
        kp_input_stock_form = kp_input_stock_Form(request.POST)
        if kp_input_stock_form.is_valid():
            kp_input_stock_form.save()
            return redirect('/data_input_kp_stock')

    context = {'input_menu_toggle':input_menu_toggle,
               'kp_inputs':kp_inputs,
               'kp_input_stock_form':kp_input_stock_form,
               'kp_stock':kp_stock,
               }
    return render(request,'dashboard/data_input_kp_stocks.html', context)

def kps_edit_stock(request, pk):
    text = kp_input_stock.objects.get(pk=pk)
    kp_input_stock_form = kp_input_stock_Form(instance=text)
    if request.method == 'POST':
        kp_input_stock_form = kp_input_stock_Form(request.POST, instance=text)
        if kp_input_stock_form.is_valid():
            kp_input_stock_form.save()
            return redirect('/data_input_kp_stock')
    context = {'kp_input_stock_form':kp_input_stock_form}
    return render(request, 'dashboard/data_input_kp_stocks.html', context)

def kps_delete_stock(request, pk):
    data = kp_input_stock.objects.get(pk=pk)
    url = "/kp_delete_stock/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/data_input_kp_stock')
    context = { 'url': url}
    return render(request, 'dashboard/delete.html', context)


def data_input_kp_recipient(request):
    input_menu_toggle = 'active'
    kp_inputs = 'active'
    kp_request_form = kp_request_Form()
    kp_request_table = kp_request.objects.exclude(purpose="-")
    if request.method == 'POST':
        kp_request_form = kp_request_Form(request.POST)
        if kp_request_form.is_valid():
            recipient_id = kp_request_form.save()
            id = recipient_id.id
            year = recipient_id.datefortable
            month = recipient_id.monthfortable
            quantity = 0

            cursor = connections['default'].cursor()
            cursor.execute("INSERT INTO kp_distribute(`Request_id`,`Quantity`,`Year`, `Month`) VALUES( %s, %s, %s, %s )", [id, quantity, year, month])
            return redirect('/data_input_kp_recipient')

    context = { 'kp_request_form':kp_request_form,
                'kp_request_table':kp_request_table,
                'kp_inputs':kp_inputs,
                'input_menu_toggle':input_menu_toggle,
                }
    return render(request, 'dashboard/data_input_kp_recipient.html', context)

def kp_recipient_edit(request, pk):
    text = kp_request.objects.get(pk=pk)
    kp_request_table = kp_request.objects.all()
    kp_request_form = kp_request_Form(instance=text)
    if request.method == 'POST':
        kp_request_form = kp_request_Form(request.POST, instance=text)
        if kp_request_form.is_valid():
            kp_request_form.save()
            return redirect('/data_input_kp_recipient')
    context = {'kp_request_form':kp_request_form,
               'kp_request_table':kp_request_table}
    return render(request, 'dashboard/data_input_kp_recipient.html', context)

def kp_recipient_delete(request, pk):
    data = kp_request.objects.get(pk=pk)
    url = "/kp_recipient_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/data_input_kp_recipient')
    context = { 'url': url}
    return render(request, 'dashboard/delete.html', context)

def kp_distribution(request, pk):
    data = kp_request.objects.get(pk=pk)
    requestee = data.requester_name
    year = data.datefortable
    month = data.monthfortable

    primary = pk
    table_data = kp_distribute.objects.filter(Request=primary).exclude(Quantity=0)
    kp_distribute_form = kp_distribute_Form()
    input_menu_toggle = 'active'
    kp_inputs = 'active'
    post = request.POST.get('action')
    if post == 'post':
        request_data = request.POST.get('request')
        kp_data = request.POST.get('kp')
        quantity_data = request.POST.get('quantity')
        # year_data = request.POST.get('year')
        # month_data = request.POST.get('month')

        cursor = connections['default'].cursor()
        cursor.execute("INSERT INTO kp_distribute(`request_id`,`kp_id`,`quantity`,`year`,`month`) VALUES( %s, %s, %s, %s, %s )", [request_data, kp_data,quantity_data,year, month])

    context = { 'kp_distribute_form':kp_distribute_form,
                'primary':primary,
                'requestee':requestee,
                'table_data':table_data,
                }
    return render(request, 'dashboard/data_input_kp_distribute.html', context)

def kp_distribution_delete(request, pk):
    data = kp_distribute.objects.raw('SELECT id, Request_id FROM kp_distribute WHERE id=%s',[pk])
    for x in data:
        x.id
        x.Request_id

    data2 = kp_request.objects.raw('SELECT id FROM kp_request WHERE id=%s', [x.Request_id])
    for y in data2:
        y.id
    dataurl = y.id

    url = "/data_input_kp_distribute_delete/" + pk
    if request.method == 'POST':
        cursor = connections['default'].cursor()
        cursor.execute('DELETE FROM kp_distribute WHERE id=%s', [pk])
        return redirect("data_input_kp_distribute", pk=dataurl)
    context = { 'url': url}
    return render(request, 'dashboard/delete.html', context)


def kp_table(request):
    kps = 'active'
    label = []
    total_kp = []
    total_kp_date = []

    accordion = []
    arnm = []
    book = []
    bnl= []
    calendar = []
    comics = []
    fa = []
    flipchart = []
    handout = []
    infographic=[]
    journal =[]
    magasin = []
    magazine = []
    mnfg = []
    poster = []
    qna= []
    rndh = []
    rs4dm = []
    technoguide = []
    tb = []

    total_request = []
    total_request_date = []
    label_occupation = []
    aew = []
    chef = []
    dw = []
    entre = []
    farmer = []
    ge = []
    go = []
    media = []
    ofw = []
    ps = []
    policy = []
    pc = []
    pm = []
    researcher = []
    student = []
    teacher = []
    others = []

    distributed = []
    distribute_year = []
    Total= []
    Total_datefortable = []
    Male=[]
    Female=[]
    Datefortable=[]

    distribute_yr2021_data=[]

    produce_yr2021_data=[]

    request_yr2021_data = []

    recipient_yr2021_data = []

    male_yr2021_data = []

    female_yr2021_data = []

    for data in kp_input.objects.raw('SELECT id, CONVERT(COUNT(title), UNSIGNED) as total, datefortable  FROM kp_input WHERE title!="-" GROUP BY datefortable ORDER BY datefortable'):
        total_kp.append(data.total)
        total_kp_date.append(data.datefortable)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total, datefortable FROM `kp_input` WHERE type="Accordion" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        accordion.append(data.total)
        label.append(data.datefortable)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="AR and Milestone" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        arnm.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Book" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        book.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Brochure and Leaflets" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        bnl.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Calendar" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        calendar.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Comics" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        comics.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Facebook Ads" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        fa.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Flipchart" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        flipchart.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Handouts" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        handout.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Infographics" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        infographic.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Journal" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        journal.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Magasin" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        magasin.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Magazine" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        magazine.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Manuals and Field Guides" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        mnfg.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Poster" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        poster.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Q&A" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        qna.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="R&D Highlights" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        rndh.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="RS4DM" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        rs4dm.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Technoguide" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        technoguide.append(data.total)

    for data in kp_input.objects.raw('SELECT id, COUNT(id) as total FROM `kp_input` WHERE type="Technology Bulletin" AND title!="-" GROUP BY datefortable ORDER BY datefortable'):
        tb.append(data.total)

    for data in kp_request.objects.raw('SELECT id, CONVERT(COUNT(purpose), UNSIGNED) as total, datefortable FROM `kp_request` WHERE purpose!="-" GROUP BY datefortable'):
        total_request.append(data.total)
        total_request_date.append(data.datefortable)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total, datefortable  FROM `kp_request` WHERE recipient_occupation="AEW" AND purpose!="-"  GROUP BY datefortable ORDER BY datefortable'):
        aew.append(data.total)
        label_occupation.append(data.datefortable)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Chef" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        chef.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Dev Worker" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        dw.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Entrepreneur" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        entre.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Farmers" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        farmer.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Govt Employee" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        ge.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Govt Officials" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        go.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Media" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        media.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="OFW" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        ofw.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="PhilRice Staff" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        ps.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Policymakers" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        policy.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Private Company" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        pc.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Program Manager" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        pm.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Researcher" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        researcher.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Student" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        student.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Teacher" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        teacher.append(data.total)

    for data in kp_request.objects.raw('SELECT id, COUNT(id) as total  FROM `kp_request` WHERE recipient_occupation="Others" AND purpose!="-" GROUP BY datefortable ORDER BY datefortable'):
        others.append(data.total)

    for data in kp_distribute.objects.raw('SELECT kp_distribute.id, kp_distribute.Year AS Year, CONVERT(SUM(kp_distribute.Quantity), UNSIGNED) AS distribute FROM kp_input LEFT JOIN kp_distribute ON kp_input.id = kp_distribute.Kp_id WHERE kp_input.title!="-" GROUP BY kp_distribute.Year'):
        distribute_year.append(data.Year)
        distributed.append(data.distribute)

    for data in kp_request.objects.raw('SELECT id, CONVERT(SUM(total),UNSIGNED) as total, datefortable FROM( SELECT id, CONVERT(SUM(recipient_male), UNSIGNED) AS total, datefortable FROM kp_request GROUP BY datefortable UNION ALL SELECT id, CONVERT(SUM(recipient_female), UNSIGNED) AS total, datefortable FROM kp_request GROUP BY datefortable ) as t GROUP BY datefortable'):
        Total.append(data.total)
        Total_datefortable.append(data.datefortable)

    for data in kp_request.objects.raw('SELECT id, CONVERT(SUM(recipient_male), UNSIGNED) AS male, CONVERT(SUM(recipient_female), UNSIGNED) AS female, datefortable FROM `kp_request` GROUP BY datefortable'):
        Male.append(data.male)
        Female.append(data.female)
        Datefortable.append(data.datefortable)

    # need to add data annually
    # start
    for data in kp_distribute.objects.raw(""" SELECT id, CONVERT(SUM(Quantity), UNSIGNED) as Quantity, Month, Year FROM `kp_distribute` WHERE Year="2021" GROUP BY Year, Month """):
        distribute_yr2021_data.append(data.Quantity)

    for data in kp_input.objects.raw(""" SELECT id, CONVERT(IF(title="-", COUNT(title) -1, COUNT(title)),UNSIGNED) as total, datefortable, monthfortable FROM kp_input WHERE datefortable="2021" GROUP BY datefortable, monthfortable """):
        produce_yr2021_data.append(data.total)

    for data in kp_request.objects.raw(""" SELECT id, CONVERT(IF(purpose="-", COUNT(purpose) -1, COUNT(purpose)), UNSIGNED) as total, datefortable, monthfortable FROM kp_request WHERE datefortable="2021" GROUP BY datefortable,monthfortable """):
        request_yr2021_data.append(data.total)

    for data in kp_request.objects.raw(""" SELECT id, CONVERT(SUM(total),UNSIGNED) as total, datefortable, monthfortable FROM( SELECT id, CONVERT(SUM(recipient_male), UNSIGNED) AS total, datefortable, monthfortable FROM kp_request GROUP BY datefortable, monthfortable UNION ALL SELECT id, CONVERT(SUM(recipient_female), UNSIGNED) AS total, datefortable, monthfortable FROM kp_request GROUP BY datefortable, monthfortable ) as t WHERE datefortable="2021" GROUP BY datefortable, monthfortable """):
        recipient_yr2021_data.append(data.total)

    for data in kp_request.objects.raw(""" SELECT id, CONVERT(SUM(recipient_male), UNSIGNED) AS male, CONVERT(SUM(recipient_female), UNSIGNED) AS female, datefortable, monthfortable FROM kp_request WHERE datefortable="2021" GROUP BY datefortable, monthfortable """):
        male_yr2021_data.append(data.male)
        female_yr2021_data.append(data.female)


    # end

    top_location = kp_request.objects.raw('SELECT id, datefortable, monthfortable, recipient_province, COUNT(id) as total FROM `kp_request` WHERE purpose!="-" AND recipient_province!="-" GROUP BY recipient_province, datefortable, monthfortable ORDER BY total DESC, monthfortable DESC, datefortable DESC')

    context = { 'kps':kps,
                'total_kp':total_kp,
                'total_kp_date':total_kp_date,
                'total_request':total_request,
                'total_request_date':total_request_date,
                'Total':Total,
                'Total_datefortable':Total_datefortable,
                'distributed':distributed,
                'distribute_year':distribute_year,
                'Male':Male,
                'Female':Female,
                'Datefortable':Datefortable,
                'label': label,
                'accordion':accordion,
                'arnm': arnm,
                'book':book,
                'bnl':bnl,
                'calendar': calendar,
                'comics' : comics,
                'fa':fa,
                'flipchart': flipchart,
                'handout':handout,
                'infographic':infographic,
                'journal':journal,
                'magasin': magasin,
                'magazine':magazine,
                'mnfg':mnfg,
                'poster':poster,
                'qna':qna,
                'rndh': rndh,
                'rs4dm':rs4dm,
                'technoguide':technoguide,
                'tb':tb,
                'label_occupation': label_occupation,
                'aew' : aew,
                'chef' : chef,
                'dw':dw,
                'entre':entre,
                'farmer':farmer,
                'ge':ge,
                'go': go,
                'media' :media,
                'ofw': ofw,
                'ps': ps,
                'policy': policy,
                'pc':pc,
                'pm': pm,
                'researcher':researcher,
                'student':student,
                'teacher' :teacher,
                'others': others,
                'top_location':top_location,
                'distribute_yr2021_data':distribute_yr2021_data,
                'produce_yr2021_data': produce_yr2021_data,
                'request_yr2021_data' : request_yr2021_data,
                'recipient_yr2021_data':recipient_yr2021_data,
                'male_yr2021_data':male_yr2021_data,
                'female_yr2021_data':female_yr2021_data,
    }
    return render(request,'dashboard/kp_tables.html',context)

def kp_stock_view(request):
    kps = 'active'

    accordion = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Accordion" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    arnm = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="AR and Milestone" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    book = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Book" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    bnl = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Brochure and Leaflets" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    calendar = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Calendar" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    comic = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Comics" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    fa = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Facebook Ads" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    flipchart = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Flipchart" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    handout = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Handouts" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    infographic = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Infographics" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    journal = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Journal" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    magasin = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Magasin" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    magazine = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Magazine" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    mnfg = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Manuals and Field Guides" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    poster = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Poster" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    qna = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Q&A" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    rndh = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="R&D Highlights" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    rs4dm = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="RS4DM" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    technoguide = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Technoguide" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')
    tb = kp_input.objects.raw('SELECT * FROM kp_input LEFT JOIN (SELECT kp_input_stock.kp_id, SUM(kp_input_stock.stocks) AS stock, kp_input_stock.printing_press FROM kp_input_stock GROUP BY kp_input_stock.kp_id ORDER BY kp_input_stock.kp_id DESC) kp_input_stock ON kp_input_stock.kp_id = kp_input.id LEFT JOIN (SELECT kp_distribute.Kp_id, SUM(kp_distribute.Quantity) AS distribute FROM kp_distribute GROUP BY kp_distribute.Kp_id) kp_distribute ON kp_distribute.Kp_id = kp_input.id WHERE kp_input.type="Technology Bulletin" AND title!="-" GROUP BY kp_input.id ORDER BY kp_input.id DESC')

    context = {'accordion':accordion,
               'arnm':arnm,
               'book':book,
               'bnl':bnl,
               'calendar':calendar,
               'comic':comic,
               'fa':fa,
               'flipchart':flipchart,
               'handout':handout,
               'infographic':infographic,
               'journal':journal,
               'magasin':magasin,
               'magazine':magazine,
               'mnfg':mnfg,
               'poster':poster,
               'qna':qna,
               'rndh':rndh,
               'rs4dm':rs4dm,
               'technoguide':technoguide,
               'tb':tb,
               'kps':kps}

    return render(request,'dashboard/kp_stock_view.html',context)

# endkp
# partners
def data_input_partners(request):
    input_menu_toggle = 'active'
    partner_input = 'active'
    partners_form = partners_Form()
    if request.method == 'POST':
        partners_form = partners_Form(request.POST)
        if partners_form.is_valid():
            partners_form.save()
            return redirect('/data_input_partners')

    context = {'partners_form': partners_form,
                'partner_input':partner_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request, 'dashboard/data_input_partners.html', context)
def partner_data(request):
    reportndata = 'active'
    parter_table = 'active'
    text = partners.objects.all()
    context = {'text':text,
    'reportndata':reportndata,
    'parter_table':parter_table}
    return render(request, 'dashboard/partners_data.html', context)
def partner_edit(request, pk):
    text = partners.objects.get(pk=pk)
    partners_form = partners_Form(instance=text)
    if request.method == 'POST':
        partners_form = partners_Form(request.POST, instance=text)
        if partners_form.is_valid():
            partners_form.save()
            return redirect('/partners')
    context = {'partners_form':partners_form}
    return render(request, 'dashboard/data_input_partners.html', context)
def partner_delete(request, pk):
    data = partners.objects.get(pk=pk)
    url = "/partners_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/partners')
    context = { 'url': url}
    return render(request, 'dashboard/delete.html', context)

def partner(request):
    partner = 'active'
    label=[]
    engagement = []
    media = []
    ngo = []
    private = []
    national = []
    regional = []
    community = []

    engagement_trend_2017 = []
    engagement_trend_2018 = []
    engagement_trend_2019 = []
    engagement_trend_2020 = []
    engagement_trend_2021 = []

    for data in partners.objects.raw('SELECT id, COUNT(engagement) as engagement, year FROM partners GROUP BY year ORDER BY year'):
        label.append(data.year)
        engagement.append(data.engagement)

    for data in partners.objects.raw('SELECT id, COUNT(classification) as media FROM partners WHERE classification="media" GROUP BY year ORDER BY year'):
        media.append(data.media)

    for data in partners.objects.raw('SELECT id, COUNT(classification) as ngo FROM partners WHERE classification="ngo" GROUP BY year ORDER BY year'):
        ngo.append(data.ngo)

    for data in partners.objects.raw('SELECT id, COUNT(scope) as national FROM partners WHERE scope="national" GROUP BY year ORDER BY year'):
        national.append(data.national)

    for data in partners.objects.raw('SELECT id, COUNT(scope) as regional FROM partners WHERE scope="regional" GROUP BY year ORDER BY year'):
        regional.append(data.regional)

    for data in partners.objects.raw('SELECT id, COUNT(scope) as community FROM partners WHERE scope="community" GROUP BY year ORDER BY year'):
        community.append(data.community)

    partner_data = partners.objects.raw('SELECT id, partner, engagement, location, startDate, endDate, month, year FROM `partners` ORDER BY year, month')

    # update yearly
    for data in partners.objects.raw(""" SELECT id, CONVERT(COUNT(engagement), UNSIGNED) as engagement, year, month FROM `partners` WHERE year='2017' GROUP BY month"""):
        engagement_trend_2017.append(data.engagement)
    for data in partners.objects.raw(""" SELECT id, CONVERT(COUNT(engagement), UNSIGNED) as engagement, year, month FROM `partners` WHERE year='2018' GROUP BY month"""):
        engagement_trend_2018.append(data.engagement)
    for data in partners.objects.raw(""" SELECT id, CONVERT(COUNT(engagement), UNSIGNED) as engagement, year, month FROM `partners` WHERE year='2019' GROUP BY month"""):
        engagement_trend_2019.append(data.engagement)
    for data in partners.objects.raw(""" SELECT id, CONVERT(COUNT(engagement), UNSIGNED) as engagement, year, month FROM `partners` WHERE year='2020' GROUP BY month"""):
        engagement_trend_2020.append(data.engagement)
    for data in partners.objects.raw(""" SELECT id, CONVERT(COUNT(engagement), UNSIGNED) as engagement, year, month FROM `partners` WHERE year='2021' GROUP BY month"""):
        engagement_trend_2021.append(data.engagement)

    # update yealy end
    context = {
    'partner': partner,
    'label' : label,
    'engagement' : engagement,
    'media' : media,
    'ngo' : ngo,
    'private' : private,
    'national' : national,
    'regional' : regional,
    'community' : community,
    'partner_data':partner_data,

    'engagement_trend_2017':engagement_trend_2017,
    'engagement_trend_2018':engagement_trend_2018,
    'engagement_trend_2019':engagement_trend_2019,
    'engagement_trend_2020':engagement_trend_2020,
    'engagement_trend_2021':engagement_trend_2021,
    }
    return render(request,'dashboard/partners.html',context)
#end partners
def data_input_intermediaries(request):
    intermediaries_form = intermediaries_Form()

    context = {'intermediaries_form':intermediaries_form}
    return render(request, 'dashboard/data_input_intermediaries.html', context)
#devcom
def data_input_progproj(request):
    input_menu_toggle = 'active'
    prog_proj_input = 'active'
    progproj_form = progproj_Form()
    if request.method == 'POST':
        progproj_form = progproj_Form(request.POST, request.FILES)
        if progproj_form.is_valid():
            progproj_form.save()
            return redirect('/data_input_progproj')

    context = {'progproj_form': progproj_form,
                'prog_proj_input':prog_proj_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request, 'dashboard/data_input_progproj.html', context)
def programprojects(request):
    devcom = 'active'
    progroj = 'active'
    program = progproj.objects.all()

    context = {
    'program' : program,
    'devcom': devcom,
    'progroj':progroj,
    }
    return render(request, 'dashboard/progproj.html', context)
def programprojects_edit(request, pk):

    program = progproj.objects.get(pk=pk)
    progproj_form = progproj_Form(instance=program)
    if request.method == 'POST':
        progproj_form = progproj_Form(request.POST, instance=program)
        if progproj_form.is_valid():
            progproj_form.save()
            return redirect('/progproj')

    context = {'progproj_form': progproj_form}
    return render(request, 'dashboard/data_input_progproj.html', context)
def programprojects_delete(request, pk):
    data = progproj.objects.get(pk=pk)
    url = "/progproj_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/progproj')
    context = { 'url': url}
    return render(request, 'dashboard/delete.html', context)

def data_input_publication(request):
    input_menu_toggle = 'active'
    prog_proj_input = 'active'
    publication_form = publication_Form()
    if request.method == 'POST':
        publication_form = publication_Form(request.POST)
        if publication_form.is_valid():
            publication_form.save()
            return redirect('/data_input_publication')

    context = {'publication_form': publication_form,
                'prog_proj_input':prog_proj_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request, 'dashboard/data_input_publication.html', context)
def publications(request):
    devcom = 'active'
    publications = 'active'
    book = publication.objects.all()
    context = {
        'book':book,
        'devcom': devcom,
        'publications':publications,
        }
    return render(request, 'dashboard/publications.html', context)
def publications_edit(request, pk):

    book = publication.objects.get(pk=pk)
    publication_form = publication_Form(instance=book)
    if request.method == 'POST':
        publication_form = publication_Form(request.POST, instance=book)
        if publication_form.is_valid():
            publication_form.save()
            return redirect('/publications')

    context = {'publication_form': publication_form}
    return render(request, 'dashboard/data_input_publication.html', context)
def publications_delete(request, pk):
    data = publication.objects.get(pk=pk)
    url = "/publications_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/publications')
    context = { 'url': url }
    return render(request, 'dashboard/delete.html',context)

def data_input_awards(request):
    input_menu_toggle = 'active'
    prog_proj_input = 'active'
    awards_form = awards_Form()
    if request.method == 'POST':
        awards_form = awards_Form(request.POST)
        if awards_form.is_valid():
            awards_form.save()
            return redirect('/data_input_awards')

    context = {'awards_form': awards_form,
                'prog_proj_input':prog_proj_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request, 'dashboard/data_input_awards.html', context)
def award(request):
    devcom = 'active'
    award = 'active'
    list = awards.objects.all()
    context = {
        'awards':list,
        'devcom': devcom,
        'award':award,
        }
    return render(request,'dashboard/awards.html', context)
def award_edit(request, pk):
    list = awards.objects.get(pk=pk)
    awards_form = awards_Form(instance=list)
    if request.method == 'POST':
        awards_form = awards_Form(request.POST, instance=list)
        if awards_form.is_valid():
            awards_form.save()
            return redirect('/awards')
    context = {'awards_form':awards_form}
    return render(request, 'dashboard/data_input_awards.html', context)
def award_delete(request, pk):
    data = awards.objects.get(pk=pk)
    url = "/awards_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/awards')
    context = { 'url': url }
    return render(request, 'dashboard/delete.html', context)

def data_input_staff(request):
    input_menu_toggle = 'active'
    prog_proj_input = 'active'
    staff_form = staff_Form(request.POST, request.FILES)
    if request.method == 'POST':
        if staff_form.is_valid():
            staff_form.save()
            return redirect('/data_input_staff')

    context = {'staff_form': staff_form,
                'prog_proj_input':prog_proj_input,
                'input_menu_toggle':input_menu_toggle}
    return render(request, 'dashboard/data_input_staff.html', context)
def staffs(request):
    devcom = 'active'
    staf = 'active'
    staffs = staff.objects.all()
    context = {
        'staffs':staffs,
        'devcom': devcom,
        'staf':staf
        }
    return render(request, 'dashboard/staffs.html', context)
def staffs_edit(request, pk):
    staffs = staff.objects.get(pk=pk)
    staff_form = staff_Form(instance=staffs)
    if request.method == 'POST':
        staff_form = staff_Form(request.POST, instance=staffs)
        if staff_form.is_valid():
            staff_form.save()
            return redirect('/staffs')
    context = {'staff_form': staff_form}
    return render(request, 'dashboard/data_input_staff.html', context)
def staffs_delete(request, pk):
    data = staff.objects.get(pk=pk)
    url = "/staffs_delete/" + pk
    if request.method == 'POST':
        data.delete()
        return redirect('/staffs')
    context = { 'url': url }
    return render(request, 'dashboard/delete.html', context)
#end devcom
#end of datainput
