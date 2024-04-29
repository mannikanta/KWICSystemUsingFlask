from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from urllib.parse import urlparse
import CircularShift as cs;
import FileReaderInput as fileReaderIn;
import NoiseWordsElimination as nwe;
import CustomSort as sort
import WriteIntoXML as winxml;
app = Flask(__name__)

@app.route('/',methods=['GET'])
def displayHomepage():
    return  render_template('/homepage.html', title="Home Page")

@app.route('/generate', methods=['GET'])
def handleController():
    output= []
    full_url = request.url
    parsed_url = urlparse(full_url)
    base_url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
    noise_words_list = fileReaderIn.read_data_from_file("./NoiseWords.txt");
    sentence = request.args.get('sentence')
    sentencesList = cs.circular_shift_words_for_all_sentences(sentence);
    sentencesList = nwe.eliminate_sentences_starting_with_noise_words(sentencesList,noise_words_list);
    sorted_sentences = sorted(sentencesList, key=sort.custom_sort_key)
    winxml.saveToXMLfile(sorted_sentences);
    for s in sorted_sentences:
        print(base_url+" "+s);
        output.append(base_url+" "+s);
    return jsonify(output);

@app.route('/retrieve',methods=['POST'])
def retrieveHandler():
    request_data = request.get_json()
    searchText = request_data.get('searchText');
    print(searchText);
    sentencesList = winxml.readDataFromXML('./resources/sentences.xml', searchText);
    for s in sentencesList:
        print(s);
    if sentencesList == '':
        return 'no sentences found with the given search word';
    else:
        return sentencesList;


if __name__ == '__main__':
    app.run(debug=True)
