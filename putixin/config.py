# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/002_config.ipynb (unless otherwise specified).

__all__ = ['CfgNode']

# Cell
import copy

# Cell
class CfgNode(dict):
    """
    CfgNode represents an internal node in the configuration tree. It's a simple
    dict-like container that allows for attribute-based access to keys.
    """
    def __init__(self, init_dict=None):
        init_dict = {} if init_dict is None else init_dict
        init_dict = self._create_config_tree_from_dict(init_dict)
        super(CfgNode, self).__init__(init_dict)

    @classmethod
    def _create_config_tree_from_dict(cls, dic):
        dic = copy.deepcopy(dic)
        for k, v in dic.items():
            if isinstance(v, dict):
                dic[k] = cls(v)
            else:
                raise Exception('is not a dictionary.')
        return dic

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value

    def __str__(self):
        def _indent(s_, num_spaces):
            s = s_.split("\n")
            if len(s) == 1:
                return s_
            first = s.pop(0)
            s = [(num_spaces * " ") + line for line in s]
            s = "\n".join(s)
            s = first + "\n" + s
            return s

        r = ""
        s = []
        for k, v in sorted(self.items()):
            seperator = "\n" if isinstance(v, CfgNode) else " "
            attr_str = "{}:{}{}".format(str(k), seperator, str(v))
            attr_str = _indent(attr_str, 2)
            s.append(attr_str)
        r += "\n".join(s)
        return r

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, super(CfgNode, self).__repr__())