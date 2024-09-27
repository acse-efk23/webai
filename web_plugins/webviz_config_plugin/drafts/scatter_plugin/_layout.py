from typing import Callable, List

import webviz_core_components as wcc

from dash import html

######################################################################
#
# Collection of Dash layout and ID-ownership
#
# Defines the Dash layout, and builds the HTML-element structure
# for the plugin.
#
# Ownership of the layout element ID's, which is provided to the
# various callback Inputs, States and Outputs.
#
######################################################################

# pylint: disable = too-few-public-methods
class LayoutElements:
    """
    Definition of names/ID's of HTML-elements in view

    Layout file is owner of ID's and provides the definition to the users,
    e.g. callbacks (Input, State and Output properties).

    NOTE: Other solutions can be used, the main goal is to have a set of defined
    names for element ID which is provided to callbacks - preventing hard coded
    string values.
    """

    GRAPH = "graph"

    ATTRIBUTE_SELECTION_DROPDOWN = "attribute_selection_dropdown"
    DATE_SELECTION_DROPDOWN = "date_selection_dropdown"
    NUMBER_OF_BINS = "number_of_bins"


def main_layout(
        get_uuid: Callable, 
        attribute_names: List[str],
        dates: List[str],
        ) -> wcc.FlexBox:
    return wcc.FlexBox(
        children=[
            wcc.FlexColumn(
                children=wcc.Frame(
                    style={"height": "90vh"},
                    children=[


                        wcc.Selectors(
                            label="Attribute Selection",
                            children=[

                                html.Div([
                                    
                                    html.Div([
                                        html.Label('Attributes', style={'font-weight': 'bold'}),
                                        wcc.Dropdown(
                                            id=get_uuid(LayoutElements.ATTRIBUTE_SELECTION_DROPDOWN),
                                            clearable=False,
                                            options=[{"label": name, "value": name} for name in attribute_names],
                                            value='PRESSURE',
                                        )
                                    ], style={'padding': '5px'}),
                                    
                                    html.Div([
                                        html.Label('Dates', style={'font-weight': 'bold'}),
                                        wcc.Dropdown(
                                            id=get_uuid(LayoutElements.DATE_SELECTION_DROPDOWN),
                                            clearable=False,
                                            options=[{"label": name, "value": name} for name in dates],
                                            value=dates[2],
                                        )
                                    ], style={'padding': '5px'}),

                                    # slider for histogram bins
                                    html.Div([
                                        html.Label('Number of bins', style={'font-weight': 'bold'}),
                                        wcc.Slider(
                                            id=get_uuid(LayoutElements.NUMBER_OF_BINS),
                                            min=1,
                                            max=50,
                                            step=1,
                                            value=10,
                                            marks={i: str(i) for i in range(0, 50, 10)},
                                        )
                                    ], style={'padding': '5px'}),


                                ], style={'display': 'flex', 'flex-direction': 'column'}),

                            ]
                        ),


                    ],
                )
            ),
            wcc.FlexColumn(
                flex=4,
                children=[
                    wcc.Frame(
                        style={"height": "90vh"},
                        highlight=False,
                        color="white",
                        children=wcc.Graph(
                            style={"height": "85vh"},
                            id=get_uuid(LayoutElements.GRAPH),
                        ),
                    )
                ],
            ),
        ],
    )
