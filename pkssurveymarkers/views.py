from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import folium
from folium import plugins
from folium.plugins import MeasureControl
from folium.plugins import MousePosition
from folium.plugins import LocateControl


# Create your views here.
def points(request):
    return render(request, 'points.html')


def front_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("map")
            else:
                return HttpResponse("No Permitted!!")
        else:
            return HttpResponse("Outsider!!")
    else:
        pass
    return render(request, 'registration/front.html')


@login_required(login_url=settings.LOGIN_URL)
def map(request):
    # Map functionality
    global locations
    m = folium.Map(location=[1.6316, 110.1926], zoom_start=17, max_zoom=19, tiles='cartoDB positron', width='90%',
                   height='75%', left='5%', position='relative')
    basemaps = {
        'Google Satelite': folium.TileLayer(
            tiles='http://mt1.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',
            attr='Google',
            name='Google Satellite',
            overlay=True,
            control=True
        )
    }
    for basemap, tilelyr in basemaps.items():
        basemaps[basemap].add_to(m)

    # REGISTER LAYER
    p_layer = folium.map.FeatureGroup()
    tbm_layer = folium.map.FeatureGroup()
    bm_layer = folium.map.FeatureGroup()
    ss_layer = folium.map.FeatureGroup()
    pks_layer = folium.map.FeatureGroup()
    line_layer = folium.map.FeatureGroup()
    #semua_point = folium.map.FeatureGroup()
    # antpath_layer = folium.map.FeatureGroup()

    # ---------------------------------------------------SHOW PKS POINTS----------------------------------------------------
    locations_pks = [
        {'loc': [1.633158697, 110.1937933],
         'popup': """<h3> PKS10</h3><br>E 2056161.701<br>N 5180634.708<p><img src="/static/MEDIA/missing.png" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.633167153, 110.1922107],
         'popup': """<h3> PKS20</h3><br>E 2055985.601<br>N 5180635.657<p><img src="/static/MEDIA/PKS20.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.632784194, 110.1917204],
         'popup': """<h3> PKS30</h3><br>E 2055931.041<br>N 5180593.316<p><img src="/static/MEDIA/PKS30.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.632259289, 110.1914934],
         'popup': """<h3> PKS40</h3><br>E 2055905.774<br>N 5180535.277<p><img src="/static/MEDIA/PKS40.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.631062247, 110.1914741],
         'popup': """<h3> PKS50</h3><br>E 2055903.613<br>N 5180402.916<p><img src="/static/MEDIA/missing.png" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.630264511, 110.1922735],
         'popup': """<h3> PKS60</h3><br>E 2055992.561<br>N 5180314.700<p><img src="/static/MEDIA/missing.png" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.629817481, 110.1930146],
         'popup': """<h3> PKS70</h3><br>E 2056075.026<br>N 5180265.264<p><img src="/static/MEDIA/PKS70.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.629972264, 110.1937932],
         'popup': """<h3> PKS80</h3><br>E 2056161.666<br>N 5180282.372<p><img src="/static/MEDIA/PKS80.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.632103719, 110.1938860],
         'popup': """<h3> PKS90</h3><br>E 2056172.002<br>N 5180518.054<p><img src="/static/MEDIA/missing.png" style="width:100%; height:100%;"></p>"""}
    ]
    for locations in locations_pks:
        pks_layer.add_child(
            folium.Circle(location=locations['loc'], radius=1, color='red', tooltip='Click For PKS info',
                          popup=folium.Popup(locations['popup'], max_width=1000)))
        pks_layer.layer_name = 'PKS MARK LOCATIONS'
        m.add_child(pks_layer)

    # ---------------------------------------------------SHOW SS POINTS-----------------------------------------------------
    locations_ss = [
        {'loc': [1.630044308, 110.1955946],
         'popup': """<h3>SS7063</h3><br>E 2056362.116<br>N 5180290.322<br>Ht. 32.920<p><img src="/static/MEDIA/SS7063.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.630071378, 110.1925468],
         'popup': """<h3>SS7064</h3><br>E 2056022.970<br>N 5180293.342<br>Ht. 29.850<p><img src="/static/MEDIA/SS7064.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.628047858, 110.1938521],
         'popup': """<h3>SS7065</h3><br>E 2056168.202<br>N 5180069.582<br>Ht. 42.420<p><img src="/static/MEDIA/missing.png" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.629850497, 110.1902865],
         'popup': """<h3>SS7066</h3><br>E 2055771.466<br>N 5180268.938<br>Ht. 46.150<p><img src="/static/MEDIA/missing.png" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.632167308, 110.1909990],
         'popup': """<h3>SS7067</h3><br>E 2055850.765<br>N 5180525.110<br>Ht. 55.390<p><img src="/static/MEDIA/missing.png" style="width:100%; height:100%;"></p>"""}
    ]
    for locations in locations_ss:
        ss_layer.add_child(folium.Circle(location=locations['loc'], radius=1, color='blue', tooltip='Click For SS info',
                                         popup=folium.Popup(locations['popup'], max_width=100)))
        ss_layer.layer_name = 'SS MARK LOCATIONS'
        m.add_child(ss_layer)

    # --------------------------------------------------SHOW TBM POINTS-----------------------------------------------------
    locations_tbm = [
        {'loc': [1.632665175, 110.1937752],
         'popup': """<h3>TBM1</h3><br>E 2056159.680<br>N 5180580.137<br>Ht. 33.448<p><img src="/static/MEDIA/TBM1.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.629769508, 110.1934765],
         'popup': """<h3>TBM2</h3><br>E 2056126.417<br>N 5180259.955<br>Ht. 27.707<p><img src="/static/MEDIA/missing.png" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.631101997, 110.1916838],
         'popup': """<h3>TBM3</h3><br>E 2055926.955<br>N 5180407.309<br>Ht. 34.202<p><img src="/static/MEDIA/TBM3.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.633132358, 110.1918806],
         'popup': """<h3>TBM4</h3><br>E 2055948.874<br>N 5180631.812<br>Ht. 33.415<p><img src="/static/MEDIA/TBM4.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.632694172, 110.1948010],
         'popup': """<h3>TBM5</h3><br>E 2056273.830<br>N 5180583.334<br>Ht. 39.456<p><img src="/static/MEDIA/TBM5.jpeg" style="width:100%; height:100%;"></p>"""}
    ]
    for locations in locations_tbm:
        tbm_layer.add_child(
            folium.Circle(location=locations['loc'], radius=1, color='black', tooltip='Click For TBM info',
                          popup=folium.Popup(locations['popup'], max_width=100)))
        tbm_layer.layer_name = 'TBM LOCATIONS'
        m.add_child(tbm_layer)

    # --------------------------------------------------SHOW BM POINTS------------------------------------------------------
    locations_bm = [
        {'loc': [1.629296811, 110.1954254],
         'popup': """<h3>BM K0184</h3><br>E 2056343.273<br>N 5180207.670<br>Ht. 32.149<p><img src="/static/MEDIA/K0184.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.629491428, 110.1923639],
         'popup': """<h3>BM K0185</h3><br>E 2056002.614<br>N 5180229.216<br>Ht. 30.001<p><img src="/static/MEDIA/K0185.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.629611703, 110.1897966],
         'popup': """<h3>BM K0187</h3><br>E 2055716.944<br>N 5180242.538<br>Ht. 32.621<p><img src="/static/MEDIA/missing.png" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.631225458, 110.1890139],
         'popup': """<h3>BM K0188</h3><br>E 2055629.871<br>N 5180420.984<br>Ht. 36.133<p><img src="/static/MEDIA/missing.png" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.631027592, 110.1913657],
         'popup': """<h3>BM K0189</h3><br>E 2055891.559<br>N 5180399.085<br>Ht. 34.012<p><img src="/static/MEDIA/K0189.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.632611536, 110.1937414],
         'popup': """<h3>BM K0190</h3><br>E 2056155.922<br>N 5180574.206<br>Ht. 33.840<p><img src="/static/MEDIA/K0190.jpeg" style="width:100%; height:100%;"></p>"""}
    ]
    for locations in locations_bm:
        bm_layer.add_child(
            folium.Circle(location=locations['loc'], radius=1, color='purple', tooltip='Click For BM info',
                          popup=folium.Popup(locations['popup'], max_width=100)))
        bm_layer.layer_name = 'BM LOCATIONS'
        m.add_child(bm_layer)

    # ----------------------------------------------------SHOW P POINTS-----------------------------------------------------
    locations_p = [
        {'loc': [1.632465819, 110.1936739],
         'popup': """<h3>P1</h3><br>E 2056148.413<br>N 5180558.095<p><img src="/static/MEDIA/P1.jpeg" style="width:100%; height:100%;"></p>"""},
        {'loc': [1.632839319, 110.1936820],
         'popup': """<h3>P11</h3><br>E 2056149.311<br>N 5180599.394<p><img src="/static/MEDIA/missing.png" style="width:100%; height:100%;"></p>"""}
    ]
    for locations in locations_p:
        p_layer.add_child(folium.Circle(location=locations['loc'], radius=1, color='orange', tooltip='Click For P info',
                                        popup=folium.Popup(locations['popup'], max_width=100)))
        p_layer.layer_name = 'P MARKS LOCATIONS'
        m.add_child(p_layer)

    # --------------------------------------------SHOW ALL POINTS USING MARKER----------------------------------------------
    #    locations_all = locations_p + locations_bm + locations_tbm + locations_ss + locations_pks
    #    for locations in locations_all:
    #        folium.Marker(location=locations['loc'])
    #        marker = folium.map.Marker(location=locations['loc'])
    #        semua_point.add_child(marker)
    #        semua_point.layer_name = 'ALL MARKERS'
    #        m.add_child(semua_point)

    # -----------------------------------------------SHOW PKS BDIST & LINES-------------------------------------------------
    line_bering_dist = [
        {'bdist': ([1.633167153, 110.1922107], [1.633158697, 110.1937933]), 'popup': "PKS20-PKS10",
         'brgdist': """90\u00B0 18' 30"  176.103 m"""},
        {'bdist': ([1.632784194, 110.1917204], [1.633167153, 110.1922107]), 'popup': "PKS30-PKS20",
         'brgdist': """52\u00B0 11' 10"  69.062 m"""},
        {'bdist': ([1.632259289, 110.1914934], [1.632784194, 110.1917204]), 'popup': "PKS40-PKS30",
         'brgdist': """23\u00B0 31' 30"  63.300 m"""},
        {'bdist': ([1.631062247, 110.1914741], [1.632259289, 110.1914934]), 'popup': "PKS50-PKS40",
         'brgdist': """00\u00B0 56' 00"  132.379 m"""},
        {'bdist': ([1.633158697, 110.1937933], [1.632103719, 110.1938860]), 'popup': "PKS10-PKS90",
         'brgdist': """174\u00B0 57' 10"  117.108 m"""},
        {'bdist': ([1.630264511, 110.1922735], [1.631062247, 110.1914741]), 'popup': "PKS60-PKS50",
         'brgdist': """314\u00B0 45' 50"  125.274 m"""},
        {'bdist': ([1.629817481, 110.1930146], [1.630264511, 110.1922735]), 'popup': "PKS70-PKS60",
         'brgdist': """300\u00B0 56' 30"  96.148 m"""},
        {'bdist': ([1.632103719, 110.1938860], [1.629972264, 110.1937932]), 'popup': "PKS90-PKS80",
         'brgdist': """182\u00B0 30' 40"  235.909 m"""},
        {'bdist': ([1.629972264, 110.1937932], [1.629817481, 110.1930146]), 'popup': "PKS80-PKS70",
         'brgdist': """258\u00B0 49' 50"  88.313 m"""}
    ]
    # show lines
    for linebrgdist in line_bering_dist:
        lineline = folium.PolyLine(linebrgdist['bdist'], popup=folium.Popup(linebrgdist['popup'], max_width=100),
                                   color='red', weight=1)
        line_layer.add_child(lineline)
        # show bearing and dist
        attr = {'fill': 'red', 'font-size': '12'}
        line_layer.add_child(
            folium.plugins.PolyLineTextPath(lineline, linebrgdist['brgdist'], center=True, below=False, offset=11,
                                            attributes=attr))

    line_layer.layer_name = 'BEARING & DIST LINES'
    m.add_child(line_layer)

    # -------------------------------------------------EXAMPLE OF PLUGINS---------------------------------------------------
    # show antpath plugin
    # laluan1 = [[1.6324370424910457, 110.19318759441376], [1.6324370424910457, 110.19360601902007], [1.6326381265135077, 110.19359529018402], [1.632643488753821, 110.19374281167984]]
    # laluan2 = [[1.6329062385121644, 110.19335925579071], [1.6329397525094855, 110.1933579146862], [1.6329370713897233, 110.19359663128853], [1.632694430036187, 110.19359529018402], [1.6326957705962335, 110.19367441534996]]

    # antpath_layer.add_child(folium.plugins.AntPath(locations=laluan1, opacity=0.5, delay=1000))
    # antpath_layer.add_child(folium.plugins.AntPath(locations=laluan2, opacity=0.5, delay=1000))

    # antpath_layer.layer_name = 'EMERGENCY PATH'
    # m.add_child(antpath_layer)

    # show measuring functions plugin
    m.add_child(MeasureControl())
    m.save('home.html')
    # show mouse coordinate plugin
    m.add_child(MousePosition())
    m.save('home.html')
    # show user location plugin
    LocateControl().add_to(m)
    # show search plugin
    #plugins.Search(layer=pks_layer, search_zoom=6, geom_type='str').add_to(m)

    # MAKE LAYERS VISIBLE
    folium.LayerControl().add_to(m)

    # SHOW MAP ON HTML
    m = m._repr_html_()
    context = {
        'm': m,
    }
    return render(request, 'map.html', context)
