hold = json.loads(
    storage['hold_create']['response']
)['card_holds'][0]

request = {
    'uri': hold['href'],
    'payload': {
        'description': 'update this description',
        'meta': {
            'holding.for': 'user1',
            'meaningful.key': 'some.value',
        }
    }
}
