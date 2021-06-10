"""
扑克游戏

Version: 0.1
Author: yomi
Date: 2021-05-25
"""

import random

class Card(object):
    """一张牌"""

    def __init__(self, suite, face):
        # suite是花色，face是点数
        # _suite, _face说明这些属性是受保护的，需要通过property装饰器来访问
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        # 当点数为1，11，12，13时，用A，J，Q，K来表示，其他的点数就用原本的数字表示
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)
    
    def __repr__(self):
        # 通过重写__repr__方法，可以在访问实例化对象时，直接输出自己想要的内容
        return self.__str__()
    
class Poker(object):
    """一副牌"""

    def __init__(self):
        self._cards = [Card(suite, face)
                        for suite in '♠♥♣♦'
                        for face in range(1, 14)]
        self._current = 0
    
    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        """洗牌（随机乱序）"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)

class Player(object):
    """玩家"""
    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []
    
    @property
    def name(self):
        return self._name
    
    @property
    def cards_on_hand(self):
        return self._cards_on_hand
        
    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        """玩家整理手上的牌"""
        self._cards_on_hand.sort(key=card_key)


# 排序规则-先根据花色再根据点数排序
def get_key(card):
    return (card.suite, card.face)

def main():
    p = Poker()
    p.shuffle()
    players = [Player('susan'), Player('Joe'), Player('Mike'), Player('June')]
    # 每个玩家摸牌
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        print(player.cards_on_hand)

if __name__ == '__main__':
    main()
