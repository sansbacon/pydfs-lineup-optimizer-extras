# pydfs_lineup_optimizer_extras/pydfs_lineup_optimizer_extras/main.py
# -*- coding: utf-8 -*-
# Copyright (C) 2021 Eric Truett
# Licensed under the MIT License

import logging
from typing import Any, Dict

from pydfs_lineup_optimizer import Player
import pandas as pd


logging.getLogger(__name__).addHandler(logging.NullHandler())


def player_to_row(p: Player) -> Dict[str, Any]:
    """Converts player object to row of data
    
    Args:
        p (Player): Player object
        
    Returns:
        Dict[str, Any]
        
    """
    wanted = ['id', 'first_name', 'last_name', 'positions', 'team', 'salary', 'fppg']
    d = {k: v for k, v in vars(p._player).items() if k in wanted}
    d['player'] = f"{d.pop('first_name')} {d.pop('last_name')}"
    d['pos'] = d.pop('positions')[0]
    return d
    
    
def row_to_player(row):
    """Converts dataframe row to player object
       Meant to be used with itertuples

    Args:
        row (NamedTuple): named tuple from itertuples

    Returns:
        Player

    """
    return Player(
        player_id=row.Index, 
        first_name=row.player.split()[0], 
        last_name='defense' if row.pos == 'DST' else row.player.split()[-1], 
        positions=[row.pos], 
        salary=row.salary, 
        team=row.team, 
        fppg=row.points
    )
    

