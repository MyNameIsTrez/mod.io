import enum

class Status(enum.Enum):
    """Status of the game.
        0 : Not accepted
        1 : Accepted (default)
        2 : Archived (default)
        3 : Deleted
    """
    not_accepted = 0
    accepted     = 1
    archived     = 2
    deleted      = 3

class Presentation(enum.Enum):
    """
    0 : Display mods for that game in a grid on mod.io
    1 : Display mods for that game in a table on mod.io
    """
    grid  = 0
    table = 1

class Submission(enum.Enum):
    """
    0 : Mod uploads must occur via a tool created by the game developers
    1 : Mod uploads can occur from anywhere, including the website and API
    """
    restricted   = 0
    unrestricted = 1

class Curation(enum.Enum):
    """
    0 : No curation: Mods are immediately available to play
    1 : Paid curation: Mods are immediately available to play unless 
    they choose to receive donations. These mods must be accepted to be listed
    2 : Full curation: All mods must be accepted by someone to be listed
    """
    no_curation   = 0
    paid_curation = 1
    full_curation = 2

class Community(enum.IntFlag):
    """
    0 : All of the options below are disabled
    1 : Discussion board enabled
    2 : Guides and news enabled
    ? : Above options can be added together to create custom settings (e.g 3 : 
    discussion board, guides and news enabled)
    """
    def __repr__(self):
        cls = self.__class__
        if self._name_ is not None:
            return self._name_
        members, uncovered = enum._decompose(cls, self._value_)
        return '|'.join([str(m._name_ or m._value_) for m in members])

    __str__ = __repr__
    
    disabled          = 0
    discussion_boards = 1
    guides_news       = 2

class Revenue(enum.IntFlag):
    """
    0 : All of the options below are disabled
    1 : Allow mods to be sold
    2 : Allow mods to receive donations
    4 : Allow mods to be traded
    8 : Allow mods to control supply and scarcity
    ? : Above options can be added together to create custom settings (e.g 3 :
    allow mods to be sold and receive donations)
    """
    def __repr__(self):
        cls = self.__class__
        if self._name_ is not None:
            return self._name_
        members, uncovered = enum._decompose(cls, self._value_)
        return '|'.join([str(m._name_ or m._value_) for m in members])

    __str__ = __repr__

    disabled     = 0
    sold         = 1
    donations    = 2
    traded       = 4
    full_control = 5

class APIAccess(enum.IntFlag):
    """
    0 : All of the options below are disabled
    1 : Allow 3rd parties to access this games API endpoints
    2 : Allow mods to be downloaded directly (if disabled all download URLs will contain a frequently 
    changing verification hash to stop unauthorized use)
    ? : Above options can be added together to create custom settings (e.g 3 : 
    allow 3rd parties to access this games API endpoints and allow mods to be
    downloaded directly)
    """
    def __repr__(self):
        cls = self.__class__
        if self._name_ is not None:
            return self._name_
        members, uncovered = enum._decompose(cls, self._value_)
        return '|'.join([str(m._name_ or m._value_) for m in members])

    __str__ = __repr__

    disabled         = 0
    third_party      = 1
    direct_downloads = 2

class MaturityOptions(enum.Enum):
    """
    0 : Don't allow mod developpers to decide whether or not to flag their mod as 
        containing mature content (if game devs wish to handle it)
    1 : Allow mod developpers to decide whether or not to flag their mod as 
        containing mature content
    """
    forbidden = 0
    allowed   = 1

class Maturity(enum.IntFlag):
    """
    0 : None
    1 : Alcohol
    2 : Drugs
    4 : Violence
    8 : Explicit
    ? : Above options can be added together to create custom settings (e.g 3 : 
    alcohol and drugs present)
    """
    def __repr__(self):
        cls = self.__class__
        if self._name_ is not None:
            return self._name_
        members, uncovered = enum._decompose(cls, self._value_)
        return '|'.join([str(m._name_ or m._value_) for m in members])

    __str__ = __repr__

    none     = 0
    alcohol  = 1
    drugs    = 2
    violence = 4
    explicit = 8

class VirusStatus(enum.Enum):
    """
    0 : Not scanned
    1 : Scan complete
    2 : In progress
    3 : Too large to scan
    4 : File not found
    5 : Error Scanning
    """
    not_scanned   = 0
    scan_complete = 1
    in_progress   = 2
    too_large     = 3
    not_found     = 4
    error         = 5

class Visibility(enum.Enum):
    """
    0 : Hidden
    1 : Public
    """
    hidden = 0
    public = 1

class Level(enum.Enum):
    moderator = 1
    creator   = 4
    admin     = 8

class Report(enum.Enum):
    """
    0 : Generic Report
    1 : DMCA Report
    """
    generic   = 0
    dmca      = 1

class EventType(enum.Enum):
    """An enum to render all event types easy to compare."""
    file_changed  = 0
    available     = 1
    unavailable   = 2
    edited        = 3
    deleted       = 4
    team_changed  = 5
    team_join     = 6
    team_leave    = 7
    subscribe     = 8
    unsubscribe   = 9
    other         = 10   

class RatingType(enum.Enum):
    """The type of rating submitted (good, bad, neutral)"""
    good    = 1
    neutral = 0
    bad     = -1