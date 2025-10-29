/*
 * Copyright Elasticsearch B.V. and/or licensed to Elasticsearch B.V. under one
 * or more contributor license agreements. Licensed under the "Elastic License
 * 2.0", the "GNU Affero General Public License v3.0 only", and the "Server Side
 * Public License v 1"; you may not use this file except in compliance with, at
 * your election, the "Elastic License 2.0", the "GNU Affero General Public
 * License v3.0 only", or the "Server Side Public License, v 1".
 */

package org.elasticsearch.gradle.internal.doc;

import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MdSnippetParser extends SnippetParser {
    public static final Pattern SNIPPET_PATTERN = Pattern.compile("(\\s*)```(.*)");
    public static final Pattern TEST_RESPONSE_PATTERN = Pattern.compile("%\\s*TESTRESPONSE(\\[(.+)\\])?\\s*");
    public static final Pattern SOURCE_PATTERN = Pattern.compile(
        "\\[\"?source\"?(?:\\.[^,]+)?,\\s*\"?([-\\w]+)\"?(,((?!id=).)*(id=\"?([-\\w]+)\"?)?(.*))?].*"
    );

    public static final String CONSOLE_REGEX = "%\\s*CONSOLE\\s*";
    public static final String NOTCONSOLE_REGEX = "%\\s*NOTCONSOLE\\s*";
    public static final String TESTSETUP_REGEX = "%\\s*TESTSETUP\\s*";
    public static final String TEARDOWN_REGEX = "%\\s*TEARDOWN\\s*";

    public MdSnippetParser(Map<String, String> defaultSubstitutions) {
        super(defaultSubstitutions);
    }

    @Override
    protected Pattern testResponsePattern() {
        return TEST_RESPONSE_PATTERN;
    }

    protected Pattern testPattern() {
        return Pattern.compile("%\\s*TEST(\\[(.+)\\])?\\s*");
    }

    private int lastLanguageLine = 0;
    private String currentName = null;
    private String lastLanguage = null;
    private int snippetIndentation = 0;

    protected void parseLine(List<Snippet> snippets, int lineNumber, String line) {
        Matcher snippetStartMatcher = SNIPPET_PATTERN.matcher(line);
        if (snippetStartMatcher.matches()) {
            if (snippetBuilder == null) {
                String indentation = snippetStartMatcher.group(1);
                snippetIndentation = indentation.length();
                String language = snippetStartMatcher.group(2);
                snippetBuilder = newSnippetBuilder().withLineNumber(lineNumber + 1)
                    .withName(currentName)
                    .withLanguage(language)
                    .withSubstitutions(defaultSubstitutions);
                // if (lastLanguageLine == lineNumber - 1) {
                //     snippetBuilder.withLanguage(lastLanguage);
                // }
                currentName = null;
            } else {
                snippetBuilder.withEnd(lineNumber + 1);
                snippetIndentation = 0;
            }
            return;
        }

        // Source source = matchSource(line);
        // if (source.matches) {
        //     lastLanguage = source.language;
        //     lastLanguageLine = lineNumber;
        //     currentName = source.name;
        //     return;
        // }
        handleCommons(snippets, line);
    }

      @Override
    protected void handleCommons(List<Snippet> snippets, String line) {
        
        // For test markers, check the trimmed line since they can be indented
            String trimmedLine = line.trim();

        if (consoleHandled(trimmedLine, snippetBuilder)) {
            return;
        }
        if (testHandled(trimmedLine, snippetBuilder)) {
            return;
        }
        if (testResponseHandled(trimmedLine, snippetBuilder)) {
            return;
        }
        if (trimmedLine.matches(getTestSetupRegex())) {
            snippetBuilder.withTestSetup(true);
            return;
        }
        if (trimmedLine.matches(getTeardownRegex())) {
            snippetBuilder.withTestTearDown(true);
            return;
        }
        if (snippetBuilder == null) {
            // Outside
            return;
        }
        if (snippetBuilder.notFinished()) {
            // Inside
            // Strip the snippet indentation from content lines
            if (snippetIndentation > 0 && line.length() > snippetIndentation) {
                // Check if the line has the expected indentation
                String prefix = line.substring(0, Math.min(snippetIndentation, line.length()));
                if (prefix.trim().isEmpty()) {
                    line = line.substring(snippetIndentation);
                }
            }
            // We don't need the annotations
            line = line.replaceAll("<\\d+>", "");
            // nor bookmarks
            line = line.replaceAll("\\[\\^\\d+\\]", "");
            // Nor any trailing spaces
            line = line.replaceAll("\\s+$", "");
            snippetBuilder.withContent(line, true);
            return;
        }
        // Allow line continuations for console snippets within lists
        if (snippetBuilder != null && line.trim().equals("+")) {
            return;
        }
        snippets.add(snippetBuilder.build());
        snippetBuilder = null;
    }

    protected String getTestSetupRegex() {
        return TESTSETUP_REGEX;
    }

    protected String getTeardownRegex() {
        return TEARDOWN_REGEX;
    }

    protected String getNotconsoleRegex() {
        return NOTCONSOLE_REGEX;
    }

    protected String getConsoleRegex() {
        return CONSOLE_REGEX;
    }

    static Source matchSource(String line) {
        Matcher matcher = SOURCE_PATTERN.matcher(line);
        if (matcher.matches()) {
            return new Source(true, matcher.group(1), matcher.group(5));
        }
        return new Source(false, null, null);
    }
}