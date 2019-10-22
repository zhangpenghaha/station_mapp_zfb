def loc_id(ele):
    return 'new UiSelector().resourceId("{}")'.format(ele)


def loc_class_instance(ele, number):
    return 'new UiSelector().className("{}").instance({})'.format(ele, number)


def loc_id_instance(ele, number):
    return 'new UiSelector().resourceId("{}").instance({})'.format(ele, number)


def loc_text_instance(ele, number):
    return 'new UiSelector().text("{}").instance({})'.format(ele, number)

def loc_contains_text_instance(ele, number):
    return 'new UiSelector().textContains("{}").instance({})'.format(ele,number)

def loc_class(ele):
    return 'new UiSelector().className("{}")'.format(ele)



def loc_text(ele):
    return 'new UiSelector().text("{}")'.format(ele)




def loc_start_text(ele):
    return 'new UiSelector().textStartsWith("{}")'.format(ele)


def loc_contains_text(ele):
    return 'new UiSelector().textContains("{}")'.format(ele)


def loc_child_ele(parent, child):
    return '{}.childSelector({})'.format(parent, child)


def loc_child_CtoC_Number(parent, child, number):
    return 'new UiSelector().className("{}").childSelector(new UiSelector().className("{}").instance({}))'.format(
        parent, child, number)
def loc_child_ItoC_Number(parent, child, number):
    return 'new UiSelector().resourceId("{}").childSelector(new UiSelector().className("{}").instance({}))'.format(
        parent, child, number)


def loc_child_TtoT(parent, child):
    return 'new UiSelector().text("{}").childSelector(new UiSelector().text("{}"))'.format(parent, child)
def loc_child_TtoST(parent, child):
    return 'new UiSelector().text("{}").childSelector(new UiSelector().textStartsWith("{}"))'.format(parent, child)
def loc_child_TtoT_Number(parent, child,number):
    return 'new UiSelector().text("{}").childSelector(new UiSelector().text("{}").instance({}))'.format(parent, child,number)

def loc_child_TtoCT_Number(parent, child,number):
    return 'new UiSelector().text("{}").childSelector(new UiSelector().textContains("{}").instance({}))'.format(parent, child,number)

def loc_child_IDtoC_Number(parent, child,number):
    return 'new UiSelector().resourceId("{}").childSelector(new UiSelector().className("{}").instance({}))'.format(parent, child,number)


def loc_child_IDtoT_Number(parent, child,number):
    return 'new UiSelector().resourceId("{}").childSelector(new UiSelector().text("{}").instance({}))'.format(parent, child,number)
def loc_child_IDtoT(parent, child):
    return 'new UiSelector().resourceId("{}").childSelector(new UiSelector().text("{}"))'.format(parent, child)

def loc_child_IDtoID_Number(parent, child,number):
    return 'new UiSelector().resourceId("{}").childSelector(new UiSelector().resourceId("{}").instance({}))'.format(parent, child,number)
def loc_child_TtoC_Number(parent, child, number):
    return 'new UiSelector().text("{}").childSelector(new UiSelector().className("{}").instance({}))'.format(parent, child, number)

def loc_parent_ele(parent, child):
    return '{}.fromParent({})'.format(child, parent)

def loc_desc(ele):
    return 'new UiSelector().description("{}")'.format(ele)

def loc_t_parent_t(parent, child, number):
    return 'new UiSelector().text("{}").fromParent(new UiSelector().className("{}").instance({}))'.format(parent, child, number)



def loc_desc_Contains(ele):
    return 'new UiSelector().descriptionContains("{}")'.format(ele)

def loc_desc_StartsWith(ele):
    return 'new UiSelector().descriptionStartsWith("{}")'.format(ele)

def judgement(a, b):
    if a == b:
        return 1
    else:
        return 0
