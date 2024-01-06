from flask import Flask, render_template, request, jsonify, redirect
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
original_user_input = None;
@app.route('/', methods=['GET', 'POST'])


def index_one():
    user_input = ""
    if request.method == 'POST':
        user_input = request.form['search-box']
        
    target_websites = [
        "http://smart.embl-heidelberg.de/smart/show_motifs.pl",
        "https://web.expasy.org/cgi-bin/protparam/protparam",
        "https://www.ebi.ac.uk/thornton-srv/databases/cgi-bin/pdbsum/FindSequence.pl",
        # "https://www.genome.jp/tools-bin/search_motif_lib"
        "http://cello.life.nctu.edu.tw/cgi/main.cgi",
        "https://web.expasy.org/cgi-bin/protscale/protscale.pl?1"
    ]

    # results = {}
    # for url in target_websites:
    #     result = scrape_website(url, user_input)  
    #     results[url] = result

    url = target_websites[0]
    result = scrape_website(url, user_input)
    url= target_websites[1]
    result_2 = scrape_website_two(url,user_input)
    # url= "https://metacyc.org/META/blast"
    url = target_websites[2]
    result_3 = scrape_website_three(url,user_input)
    # return jsonify(results)
    url=target_websites[3]
    result_4 =scrape_website_four(url,user_input)
    url=target_websites[4]
    result_5=scrape_website_five(url,user_input)
    result_6=scrape_website_six(url,user_input)
    result_7=scrape_website_seven(url,user_input)
    result_8=scrape_website_eight(url,user_input)
    result_9=scrape_website_nine(url,user_input)
    return render_template('index.html', user_input=result,result_2=result_2,table_data=result_3,result_4=result_4,result_5=result_5,result_6=result_6,result_7=result_7,result_8=result_8,result_9=result_9)

def scrape_website(url, search_sequence):
    try:
        response = requests.post(url, data={"ID":"", "SEQUENCE": search_sequence, "DO_SMART": "Sequence SMART", "introns":"0"})
        # response = requests.post(url, data={"prot_id":"", "sequence": search_sequence, "mandatory": ""})
        # response = requests.post(url, data={"seqid":"","upload_file":"(binary)","seq": search_sequence, "pfam": "on","pfam_cuteval": "1.0","cdd_filter": "","cdd_cuteval": "1.0","skip_entry":"on","skip_unspecific_profile":"on","user_cutsore":"","profile_file":"(binary)","FORMAT":"PROSITE"})


        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # result = {"status": "success", "data": soup.find("form").text.strip()}
            flag = 0;
            for i in soup.find_all('img'):
                flag = flag + 1
                if flag==2:
                    result = i['src']
                    break
            if result:
                pass
            else:
                result="result_not_found"

            # result = soup.find("form").text.strip();
        else:
            result = {"status": "error", "message": "Request to target website failed"}
    except Exception as e:
        result = {"status": "error", "message": str(e)}

    return result
def scrape_website_two(url, search_sequence):
    result_2 = None
    try:
        # response = requests.post(url, data={"ID":"", "SEQUENCE": search_sequence, "DO_SMART": "Sequence SMART", "introns":"0"})
        response = requests.post(url, data={"prot_id":"", "sequence": search_sequence, "mandatory": ""})
        # response = requests.post(url, data={"seqid":"","upload_file":"(binary)","seq": search_sequence, "pfam": "on","pfam_cuteval": "1.0","cdd_filter": "","cdd_cuteval": "1.0","skip_entry":"on","skip_unspecific_profile":"on","user_cutsore":"","profile_file":"(binary)","FORMAT":"PROSITE"})


        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            result = {"status": "success", "data": soup.find("form").text.strip()}
            flag = 0;
            for i in soup.find_all('pre'):
                flag = flag + 1
                if flag==2:
                    result_2 = i.text.strip()
                    break
            if result:
                pass
            else:
                result="result_not_found"    
            # result_2 = soup.find("form").text.strip();
        else:
            result_2 = {"status": "error", "message": "Request to target website failed"}
    except Exception as e:
        result_2 = {"status": "error", "message": str(e)}

    return result_2
def scrape_website_three(url, search_sequence):
    try:
        # response = requests.post(url, data={"ID":"", "SEQUENCE": search_sequence, "DO_SMART": "Sequence SMART", "introns":"0"})
        # response = requests.post(url, data={"prot_id":"", "sequence": search_sequence, "mandatory": ""})
        # response = requests.post(url, data={"seqid":"","upload_file":"(binary)","seq": search_sequence, "pfam": "on","pfam_cuteval": "1.0","cdd_filter": "","cdd_cuteval": "1.0","skip_entry":"on","skip_unspecific_profile":"on","user_cutscore":"","profile_file":"(binary)","FORMAT":"PROSITE"})
        # response = requests.post(url, data={"organism":"META","dbname":"orgID()","querytype":"protein","blastBioCyc":"","blastBioCycJobId":"","blastBioCycQueueLen":"","dbtype":"protein","program":"blastp","sequence": search_sequence, "evalue": "10","seg": "no","query_gencode": "1","MAT_PARAM": "-matrix BLOSUM62 -gapopen 11 -gapextend 1","OTHER_ADVANCED":""})
        response = requests.post(url, data={"pasted": search_sequence})

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # result = {"status": "success", "data": soup.find("form").text.strip()}
            flag = 0
            for i in soup.find_all('table'):
                flag = flag + 1
                if flag==3:
                    result_3 = i
                    break
                
            table_rows = result_3.find_all('tr') if result_3 else []
            # Extract table data
            data = []
            for row in table_rows:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                data.append(cols)

            #result_3 = soup.find('table', class_ = 'result')
            # result_3 = soup.find("table").text.strip();
        else:
            data = {"status": "error", "message": "Request to target website failed"}
    except Exception as e:
        data = {"status": "error", "message": str(e)}

    return data
def scrape_website_four(url, search_sequence):
    try:
        # response = requests.post(url, data={"ID":"", "SEQUENCE": search_sequence, "DO_SMART": "Sequence SMART", "introns":"0"})
        # response = requests.post(url, data={"prot_id":"", "sequence": search_sequence, "mandatory": ""})
        # response = requests.post(url, data={"seqid":"","upload_file":"(binary)","seq": search_sequence, "pfam": "on","pfam_cuteval": "1.0","cdd_filter": "","cdd_cuteval": "1.0","skip_entry":"on","skip_unspecific_profile":"on","user_cutscore":"","profile_file":"(binary)","FORMAT":"PROSITE"})
        # response = requests.post(url, data={"organism":"META","dbname":"orgID()","querytype":"protein","blastBioCyc":"","blastBioCycJobId":"","blastBioCycQueueLen":"","dbtype":"protein","program":"blastp","sequence": search_sequence, "evalue": "10","seg": "no","query_gencode": "1","MAT_PARAM": "-matrix BLOSUM62 -gapopen 11 -gapextend 1","OTHER_ADVANCED":""})
        response = requests.post(url, data={"species": "pro","seqtype":"prot","fasta":">1086005|Genbank|Outer membrane/Extracellular (Autotransporter)|major ring-forming surface protein precursor\n"+search_sequence,"file":"(binary)","Submit":"Submit"})

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            result_4=soup.find('table')
            table_rows = result_4.find_all('tr') if result_4 else []
            # Extract table data
            result_4 = []
            for row in table_rows:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                result_4.append(cols)
        

            #result_3 = soup.find('table', class_ = 'result')
            # result_3 = soup.find("table").text.strip();
        else:
            result_4 = {"status": "error", "message": "Request to target website failed"}
    except Exception as e:
        result_4 = {"status": "error", "message": str(e)}

    return result_4
def scrape_website_five(url, search_sequence):
    result_5 = None
    try:
        # response = requests.post(url, data={"ID":"", "SEQUENCE": search_sequence, "DO_SMART": "Sequence SMART", "introns":"0"})
        # response = requests.post(url, data={"prot_id":"", "sequence": search_sequence, "scale": "Molecular weight","window":"9","weight_edges":"100","weight_var":"linear","norm":"no"})
        # response = requests.post(url, data={"seqid":"","upload_file":"(binary)","seq": search_sequence, "pfam": "on","pfam_cuteval": "1.0","cdd_filter": "","cdd_cuteval": "1.0","skip_entry":"on","skip_unspecific_profile":"on","user_cutsore":"","profile_file":"(binary)","FORMAT":"PROSITE"})

        headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
        }


        body = f"prot_id=&sequence={search_sequence}&scale=Number+of+codon%28s%29&window=9&weight_edges=100&weight_var=linear&norm=no"

        response = requests.post(url, headers=headers, data=body)
        

        soup = BeautifulSoup(response.content, 'html.parser')

        result = {"status": "success", "data": soup.find("pre")}
        flag = 0;
        for i in soup.find_all('pre'):
            flag = flag + 1
            if flag==2:
                result_5 = i.text.strip()
                break
        if result:
            pass
        else:
            result="result_not_found"    
           

    except Exception as e:
        result_5 = {"status": "error", "message": str(e)}

    return result_5
    
def scrape_website_six(url, search_sequence):
    result_6 = None
    try:
        # response = requests.post(url, data={"ID":"", "SEQUENCE": search_sequence, "DO_SMART": "Sequence SMART", "introns":"0"})
        # response = requests.post(url, data={"prot_id":"", "sequence": search_sequence, "scale": "Molecular weight","window":"9","weight_edges":"100","weight_var":"linear","norm":"no"})
        # response = requests.post(url, data={"seqid":"","upload_file":"(binary)","seq": search_sequence, "pfam": "on","pfam_cuteval": "1.0","cdd_filter": "","cdd_cuteval": "1.0","skip_entry":"on","skip_unspecific_profile":"on","user_cutsore":"","profile_file":"(binary)","FORMAT":"PROSITE"})

        headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
        }


        body = f"prot_id=&sequence={search_sequence}&scale=Molecular+weight&window=9&weight_edges=100&weight_var=linear&norm=no"

        response = requests.post(url, headers=headers, data=body)
        

        soup = BeautifulSoup(response.content, 'html.parser')

        result = {"status": "success", "data": soup.find("pre")}
        flag = 0;
        for i in soup.find_all('pre'):
            flag = flag + 1
            if flag==2:
                result_6 = i.text.strip()
                break
        if result:
            pass
        else:
            result="result_not_found"    
           

    except Exception as e:
        result_6 = {"status": "error", "message": str(e)}

    return result_6

def scrape_website_seven(url, search_sequence):
    result_7 = None
    try:
        # response = requests.post(url, data={"ID":"", "SEQUENCE": search_sequence, "DO_SMART": "Sequence SMART", "introns":"0"})
        # response = requests.post(url, data={"prot_id":"", "sequence": search_sequence, "scale": "Molecular weight","window":"9","weight_edges":"100","weight_var":"linear","norm":"no"})
        # response = requests.post(url, data={"seqid":"","upload_file":"(binary)","seq": search_sequence, "pfam": "on","pfam_cuteval": "1.0","cdd_filter": "","cdd_cuteval": "1.0","skip_entry":"on","skip_unspecific_profile":"on","user_cutsore":"","profile_file":"(binary)","FORMAT":"PROSITE"})

        headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
        }


        body = f"prot_id=&sequence={search_sequence}&scale=alpha-helix+%2F+Deleage+%26+Roux&window=9&weight_edges=100&weight_var=linear&norm=no"

        response = requests.post(url, headers=headers, data=body)
        

        soup = BeautifulSoup(response.content, 'html.parser')

        result = {"status": "success", "data": soup.find("pre")}
        flag = 0;
        for i in soup.find_all('pre'):
            flag = flag + 1
            if flag==2:
                result_7 = i.text.strip()
                break
        if result:
            pass
        else:
            result="result_not_found"    
           

    except Exception as e:
        result_7 = {"status": "error", "message": str(e)}

    return result_7

def scrape_website_eight(url, search_sequence):
    result_8 = None
    try:
        # response = requests.post(url, data={"ID":"", "SEQUENCE": search_sequence, "DO_SMART": "Sequence SMART", "introns":"0"})
        # response = requests.post(url, data={"prot_id":"", "sequence": search_sequence, "scale": "Molecular weight","window":"9","weight_edges":"100","weight_var":"linear","norm":"no"})
        # response = requests.post(url, data={"seqid":"","upload_file":"(binary)","seq": search_sequence, "pfam": "on","pfam_cuteval": "1.0","cdd_filter": "","cdd_cuteval": "1.0","skip_entry":"on","skip_unspecific_profile":"on","user_cutsore":"","profile_file":"(binary)","FORMAT":"PROSITE"})

        headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
        }


        body = f"prot_id=&sequence={search_sequence}&scale=beta-turn+%2F+Deleage+%26+Roux&window=9&weight_edges=100&weight_var=linear&norm=no"

        response = requests.post(url, headers=headers, data=body)
        

        soup = BeautifulSoup(response.content, 'html.parser')

        result = {"status": "success", "data": soup.find("pre")}
        flag = 0;
        for i in soup.find_all('pre'):
            flag = flag + 1
            if flag==2:
                result_8 = i.text.strip()
                break
        if result:
            pass
        else:
            result="result_not_found"    
           

    except Exception as e:
        result_8 = {"status": "error", "message": str(e)}

    return result_8

def scrape_website_nine(url, search_sequence):
    result_9 = None
    try:
        # response = requests.post(url, data={"ID":"", "SEQUENCE": search_sequence, "DO_SMART": "Sequence SMART", "introns":"0"})
        # response = requests.post(url, data={"prot_id":"", "sequence": search_sequence, "scale": "Molecular weight","window":"9","weight_edges":"100","weight_var":"linear","norm":"no"})
        # response = requests.post(url, data={"seqid":"","upload_file":"(binary)","seq": search_sequence, "pfam": "on","pfam_cuteval": "1.0","cdd_filter": "","cdd_cuteval": "1.0","skip_entry":"on","skip_unspecific_profile":"on","user_cutsore":"","profile_file":"(binary)","FORMAT":"PROSITE"})

        headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
        }


        body = f"prot_id=&sequence={search_sequence}&scale=Polarity+%2F+Grantham&window=9&weight_edges=100&weight_var=linear&norm=no"

        response = requests.post(url, headers=headers, data=body)
        

        soup = BeautifulSoup(response.content, 'html.parser')

        result = {"status": "success", "data": soup.find("pre")}
        flag = 0;
        for i in soup.find_all('pre'):
            flag = flag + 1
            if flag==2:
                result_9 = i.text.strip()
                break
        if result:
            pass
        else:
            result="result_not_found"    
           

    except Exception as e:
        result_9 = {"status": "error", "message": str(e)}

    return result_9
if __name__ == '__main__':
    app.run(debug=True)



