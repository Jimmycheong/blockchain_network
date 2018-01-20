@app.route("/api/blockchain",  methods=['GET'])
def get_newest_version_of_blockchain():
    chain = read_from_pickle("resources/chain.pkl")
    return json.dumps(chain)