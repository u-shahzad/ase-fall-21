from flakon import JsonBlueprint, create_app
from flask import abort, app, jsonify, request
import json
from bedrock_a_party.classes.party import CannotPartyAloneError, ItemAlreadyInsertedByUser, NotExistingFoodError, NotInvitedGuestError, Party

parties = JsonBlueprint('parties', __name__)


_LOADED_PARTIES = {}  # dict of available parties
_PARTY_NUMBER = 0  # index of the last created party


#
# These are utility functions. Use them, DON'T CHANGE THEM!!
#

def create_party(req):
    global _LOADED_PARTIES, _PARTY_NUMBER

    # get data from request
    json_data = req.get_json()

    # list of guests
    try:
        guests = json_data['guests']
    except:
        raise CannotPartyAloneError("you cannot party alone!")

    # add party to the loaded parties lists
    _LOADED_PARTIES[str(_PARTY_NUMBER)] = Party(_PARTY_NUMBER, guests)
    _PARTY_NUMBER += 1

    return jsonify({'party_number': _PARTY_NUMBER - 1})


def get_all_parties():
    global _LOADED_PARTIES

    return jsonify(loaded_parties=[party.serialize() for party in _LOADED_PARTIES.values()])


def exists_party(_id):
    global _PARTY_NUMBER
    global _LOADED_PARTIES

    if int(_id) > _PARTY_NUMBER:
        abort(404)  # error 404: Not Found, i.e. wrong URL, resource does not exist
    elif not(_id in _LOADED_PARTIES):
        abort(410)  # error 410: Gone, i.e. it existed but it's not there anymore


# TODO: complete the decoration
@parties.route("/parties", methods=['POST', 'GET'])
def all_parties():
    result = None
    
    if request.method == 'POST':
        try:
            # TODO: create a party
            guests = request.json
            p = create_party(jsonify({'guests': guests['guests']}))
            r = p.get_json()
            result = jsonify({'party_number': r['party_number']})

        except CannotPartyAloneError:
            # TODO: return 400
            abort(400)

    elif request.method == 'GET':
        # TODO: get all the parties
        result = get_all_parties()

    return result


# TODO: complete the decoration
@parties.route("/parties/loaded")
def loaded_parties():
    # TODO: returns the number of parties currently loaded in the system
    p =  get_all_parties()
    r = p.get_json()
    return jsonify({'loaded_parties': len(r['loaded_parties'])})

# TODO: complete the decoration
@parties.route("/party/<id>", methods=['DELETE', 'GET'])
def single_party(id):
    global _LOADED_PARTIES
    result = ""

    # TODO: check if the party is an existing one
    exists_party(id)

    if request.method == 'GET':
        # TODO: retrieve a party
        p = get_all_parties()
        r = p.get_json()
        result = r['loaded_parties'][int(id)]
        #print("idididid" + id)

    elif request.method == 'DELETE':
        # TODO: delete a party
        del _LOADED_PARTIES[id]

    return result


# TODO: complete the decoration
@parties.route("/party/<id>/foodlist", methods=['GET'])
def get_foodlist(id):
    global _LOADED_PARTIES
    result = ""

    # TODO: check if the party is an existing one
    exists_party(id)

    if request.method == 'GET':
        # TODO: retrieve food-list of the party
        p = get_all_parties()
        r = p.get_json()
        sp = r['loaded_parties'][int(id)]
        result = jsonify({'foodlist': sp['foodlist']})
        #print(sp['guests'])

    return result


# TODO: complete the decoration
@parties.route("/party/<id>/foodlist/<user>/<item>", methods=['POST', 'DELETE', 'GET'])
def edit_foodlist(id, user, item):
    global _LOADED_PARTIES

    # TODO: check if the party is an existing one
    exists_party(id)
    # TODO: retrieve the party
    result = ""
    p = get_all_parties()
    r = p.get_json()
    sp = r['loaded_parties'][int(id)]

    if request.method == 'POST':
        # TODO: add item to food-list handling NotInvitedGuestError (401) and ItemAlreadyInsertedByUser (400)
        try:
            if user in sp['guests'] and item not in sp['foodlist']:
                _LOADED_PARTIES[id].add_to_food_list(item, user)
                result = {'food': item, 'user': user}
        except NotInvitedGuestError or ItemAlreadyInsertedByUser:
            raise (NotInvitedGuestError, ItemAlreadyInsertedByUser)

    if request.method == 'DELETE':
        # TODO: delete item to food-list handling NotExistingFoodError (400)
        try:
            if item in sp['foodlist']:
                _LOADED_PARTIES[id].remove_from_food_list(item, user)
                result = jsonify({'msg': 'Food deleted!'})

        except NotExistingFoodError:
            raise NotExistingFoodError("Not existing food error!")

    return result