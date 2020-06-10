#coding:gbk
"""
����Ŀ�꣺ʵ��ͨ��������������һ��ݣ�1960-2015�꣩���Զ��������������GDP�����Ե�ͼ��ʽ���ӻ�����������棨��svg�ļ���ʽ��
�������ߣ���֤��
���ڣ�2020/6/10
"""
import csv
import math
import pygal
import pygal_maps_world  #�������ݿ�

def read_csv_as_nested_dict(filename, keyfield, separator, quote): #��ȡԭʼcsv�ļ������ݣ���ʽΪǶ���ֵ�
    """
    �������:
      filename:csv�ļ���
      keyfield:����
      separator:�ָ���
      quote:���÷�

    ���:
      ��ȡcsv�ļ����ݣ�����Ƕ���ֵ��ʽ����������ֵ�ļ���Ӧ����keyfiled���ڲ��ֵ��Ӧÿ���ڸ�������Ӧ�ľ���ֵ
    """
    result={}
    with open(filename,newline="")as csvfile:
        csvreader=csv.DictReader(csvfile,delimiter=separator,quotechar=quote)
        for row in csvreader:
            rowid=row[keyfield]
            result[rowid]=row

    return result
    
pygal_countries = pygal.maps.world.COUNTRIES #��ȡpygal.maps.world�й��Ҵ�����Ϣ��Ϊ�ֵ��ʽ�������м�Ϊpygal�и������룬ֵΪ��Ӧ�ľ������(���齫����ʾ����Ļ���˽�����ʽ���������ݣ�
asuka=read_csv_as_nested_dict("isp_gdp.csv","Country Name",",",'"')
#print(asuka)
def reconcile_countries_by_name(plot_countries, gdp_countries): #������������GDP���ݵĻ�ͼ����Ҵ����ֵ䣬�Լ�û������GDP���ݵĹ��Ҵ��뼯��
	"""   
	�������:
	plot_countries: ��ͼ����Ҵ������ݣ��ֵ��ʽ�����м�Ϊ��ͼ����Ҵ��룬ֵΪ��Ӧ�ľ������
	gdp_countries:���и������ݣ�Ƕ���ֵ��ʽ�������ⲿ�ֵ�ļ�Ϊ���й��Ҵ��룬ֵΪ�ù��������ļ��е������ݣ��ֵ��ʽ)
	
	�����
	����Ԫ���ʽ������һ���ֵ��һ�����ϡ������ֵ�����Ϊ��������GDP���ݵĻ�ͼ�������Ϣ����Ϊ��ͼ������Ҵ��룬ֵΪ��Ӧ�ľ������),
	��������Ϊ��������GDP���ݵĻ�ͼ����Ҵ���
	"""
	
	a={}
	c=set()
	m=tuple()    
	for i in plot_countries.keys():
		for j in gdp_countries: 
			if plot_countries[i]==j:
				a[i]=plot_countries[i]#������Ϊ��������GDP���ݵĻ�ͼ�������Ϣ����Ϊ��ͼ������Ҵ��룬ֵΪ��Ӧ�ľ������)
			if plot_countries[i]!=j:
				c.add(i)#��������Ϊ��������GDP���ݵĻ�ͼ����Ҵ���
	m=m+(a,)+(c,) #����Ԫ���ʽ         
	return(m)
	          
def build_map_dict_by_name(gdpinfo, plot_countries, year):
	"""
	�������:
	gdpinfo: 
	plot_countries: ��ͼ����Ҵ������ݣ��ֵ��ʽ�����м�Ϊ��ͼ����Ҵ��룬ֵΪ��Ӧ�ľ������
	year: �������ֵ
	
	�����
	�������һ���ֵ�Ͷ������ϵ�Ԫ�����ݡ������ֵ�����Ϊ��ͼ������Ҵ��뼰��Ӧ����ĳ�������GDP��ֵ����Ϊ��ͼ���и����Ҵ��룬ֵΪ�ھ�����ݣ���year����ȷ��������Ӧ������GDP����ֵ��Ϊ
	������ʾ���㣬GDP�����ת��Ϊ��10Ϊ�����Ķ�����ʽ����GDPԭʼֵΪ2500����ӦΪlog2500��ps:����math.log()���)
	2������һ��Ϊ������GDP��������ȫû�м�¼�Ļ�ͼ����Ҵ��룬��һ������Ϊֻ��û��ĳ�ض��꣨��year����ȷ��������GDP���ݵĻ�ͼ����Ҵ���
	"""
	a={}
	b={}
	c=set()
	d=set()
	m=tuple()
	for i in plot_countries.keys():
		for j in asuka: 
			if plot_countries[i]==j:
				a[i]=plot_countries[i]
			if plot_countries[i]!=j:
				c.add(i)#����Ϊ����GDP��������ȫû�м�¼�Ļ�ͼ����Ҵ���
	
	for i in plot_countries.keys():
		for j in asuka.values():
			if j[year]!='' and j['Country Name']==plot_countries[i]:
				number=float(j[year])
				year_number=math.log10(number)
				b[i]=year_number#�ֵ�����Ϊ��ͼ������Ҵ��뼰��Ӧ����ĳ�������GDP��ֵ����Ϊ��ͼ���и����Ҵ��룬ֵΪ�ھ������
			if j[year]=='' and j['Country Name']==plot_countries[i]:
				d.add(i)#����Ϊֻ��û��ĳ�ض��꣨��year����ȷ��������GDP���ݵĻ�ͼ����Ҵ���
	m=m+(b,)+(c,)+(d,)
	
	return(m)

def render_world_map(gdpinfo, plot_countries, year, map_file): #������ĳ�����������GDP����(����ȱ��GDP�����Լ�ֻ���ڸ���ȱ��GDP���ݵĹ���)�Ե�ͼ��ʽ���ӻ�
	"""
	Inputs:
	  
	  gdpinfo:gdp��Ϣ�ֵ�
	  plot_countires:��ͼ����Ҵ������ݣ��ֵ��ʽ�����м�Ϊ��ͼ����Ҵ��룬ֵΪ��Ӧ�ľ������
	  year:����������ݣ����ַ�����ʽ������"1970"
	  map_file:�����ͼƬ�ļ���
	
	Ŀ�꣺��ָ��ĳ����������GDP�����������ͼ����ʾ������������Ϊ����ĵ�ͼƬ�ļ�
	��ʾ�����������ӻ���Ҫ����pygal.maps.world.World()����
	 
	"""
	k=build_map_dict_by_name(gdpinfo, pygal_countries, year)
	a=k[0]
	n=[]
	for i in a.items():
		n.append(i)
	worldmap_chart = pygal.maps.world.World()
	worldmap_chart.title = 'ȫ��GDP�ֲ�ͼ'#��������
	worldmap_chart.add(year, n)#���ӻ�������ݸ������������ж�Ӧ��GDPֵ
	worldmap_chart.add('no date at this year',list(k[2]))#���ӻ�����û�����ݵĹ���
	worldmap_chart.add('missing from word bank',list(k[1]))#���ӻ�û���������ݵĹ���
	worldmap_chart.render_to_file(map_file)
	return()

def test_render_world_map(year):  #���Ժ���
    """
    �Ը����ܺ������в���
    """
    gdpinfo = {"gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"} #���������ֵ�
  
   
    pygal_countries = pygal.maps.world.COUNTRIES   # ��û�ͼ��pygal���Ҵ����ֵ�
    # ����ʱ����1970��Ϊ�����Ժ����������ԣ������н�����ṩ��svg���жԱȣ�������ݿɽ��ļ���������
    render_world_map(gdpinfo, pygal_countries, year, "isp_gdp_world_name_%s.svg"%year)
	

print("��ӭʹ������GDP���ݿ��ӻ���ѯ")
print("----------------------")
year=input("���������ѯ�ľ������:")
test_render_world_map(year)
