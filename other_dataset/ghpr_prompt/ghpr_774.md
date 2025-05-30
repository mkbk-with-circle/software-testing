## Buggy code
```java
/*
 * Copyright 2012 Benjamin Weiss
 * Copyright 2012 Neofonie Mobile GmbH
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package de.keyboardsurfer.android.widget.crouton;

import android.app.Activity;
import android.content.Context;
import android.content.res.Resources;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Shader;
import android.graphics.Typeface;
import android.graphics.drawable.BitmapDrawable;
import android.util.TypedValue;
import android.view.View;
import android.view.ViewGroup;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;

/*
 * Based on an article by Cyril Mottier (http://android.cyrilmottier.com/?p=773) <br>
 */


/**
 * Displays information in a non-invasive context related manner. Like
 * {@link android.widget.Toast}, but better.
 * <p/>
 * <b>Important: </b>
 * Call {@link Crouton#clearCroutonsForActivity(Activity)} within
 * {@link android.app.Activity#onDestroy()} to avoid {@link Context} leaks.
 */
public final class Crouton {
  private static final int IMAGE_ID = 0x100;
  private static final int TEXT_ID = 0x101;
  private final CharSequence text;
  private final Style style;
  private final View customView;

  private Activity activity;
  private ViewGroup viewGroup;
  private FrameLayout croutonView;
  private Animation inAnimation;
  private Animation outAnimation;
  private LifecycleCallback lifecycleCallback = null;

  /**
   * Creates the {@link Crouton}.
   *
   * @param activity
   *   The {@link Activity} that the {@link Crouton} should be attached
   *   to.
   * @param text
   *   The text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   */
  private Crouton(Activity activity, CharSequence text, Style style) {
    if ((activity == null) || (text == null) || (style == null)) {
      throw new IllegalArgumentException("Null parameters are not accepted");
    }

    this.activity = activity;
    this.viewGroup = null;
    this.text = text;
    this.style = style;
    this.customView = null;
  }

  /**
   * Creates the {@link Crouton}.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param text
   *   The text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   * @param viewGroup
   *   The {@link ViewGroup} that this {@link Crouton} should be added to.
   */
  private Crouton(Activity activity, CharSequence text, Style style, ViewGroup viewGroup) {
    if ((activity == null) || (text == null) || (style == null)) {
      throw new IllegalArgumentException("Null parameters are not accepted");
    }

    this.activity = activity;
    this.text = text;
    this.style = style;
    this.viewGroup = viewGroup;
    this.customView = null;
  }

  /**
   * Creates the {@link Crouton}.
   *
   * @param activity
   *   The {@link Activity} that the {@link Crouton} should be attached
   *   to.
   * @param customView
   *   The custom {@link View} to display
   */
  private Crouton(Activity activity, View customView) {
    if ((activity == null) || (customView == null)) {
      throw new IllegalArgumentException("Null parameters are not accepted");
    }

    this.activity = activity;
    this.viewGroup = null;
    this.customView = customView;
    this.style = new Style.Builder().build();
    this.text = null;
  }

  /**
   * Creates the {@link Crouton}.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param customView
   *   The custom {@link View} to display
   * @param viewGroup
   *   The {@link ViewGroup} that this {@link Crouton} should be added to.
   */
  private Crouton(Activity activity, View customView, ViewGroup viewGroup) {
    if ((activity == null) || (customView == null)) {
      throw new IllegalArgumentException("Null parameters are not accepted");
    }

    this.activity = activity;
    this.customView = customView;
    this.viewGroup = viewGroup;
    this.style = new Style.Builder().build();
    this.text = null;
  }

  /**
   * Creates a {@link Crouton} with provided text and style for a given
   * activity.
   *
   * @param activity
   *   The {@link Activity} that the {@link Crouton} should be attached
   *   to.
   * @param text
   *   The text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   *
   * @return The created {@link Crouton}.
   */
  public static Crouton makeText(Activity activity, CharSequence text, Style style) {
    return new Crouton(activity, text, style);
  }

  /**
   * Creates a {@link Crouton} with provided text and style for a given
   * activity.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param text
   *   The text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   * @param viewGroup
   *   The {@link ViewGroup} that this {@link Crouton} should be added to.
   *
   * @return The created {@link Crouton}.
   */
  public static Crouton makeText(Activity activity, CharSequence text, Style style, ViewGroup viewGroup) {
    return new Crouton(activity, text, style, viewGroup);
  }

  /**
   * Creates a {@link Crouton} with provided text and style for a given
   * activity.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param text
   *   The text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   * @param viewGroupResId
   *   The resource id of the {@link ViewGroup} that this {@link Crouton} should be added to.
   *
   * @return The created {@link Crouton}.
   */
  public static Crouton makeText(Activity activity, CharSequence text, Style style, int viewGroupResId) {
    return new Crouton(activity, text, style, (ViewGroup) activity.findViewById(viewGroupResId));
  }


  /**
   * Creates a {@link Crouton} with provided text-resource and style for a given
   * activity.
   *
   * @param activity
   *   The {@link Activity} that the {@link Crouton} should be attached
   *   to.
   * @param textResourceId
   *   The resource id of the text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   *
   * @return The created {@link Crouton}.
   */
  public static Crouton makeText(Activity activity, int textResourceId, Style style) {
    return makeText(activity, activity.getString(textResourceId), style);
  }

  /**
   * Creates a {@link Crouton} with provided text-resource and style for a given
   * activity.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param textResourceId
   *   The resource id of the text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   * @param viewGroup
   *   The {@link ViewGroup} that this {@link Crouton} should be added to.
   *
   * @return The created {@link Crouton}.
   */
  public static Crouton makeText(Activity activity, int textResourceId, Style style, ViewGroup viewGroup) {
    return makeText(activity, activity.getString(textResourceId), style, viewGroup);
  }

  /**
   * Creates a {@link Crouton} with provided text-resource and style for a given
   * activity.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param textResourceId
   *   The resource id of the text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   * @param viewGroupResId
   *   The resource id of the {@link ViewGroup} that this {@link Crouton} should be added to.
   *
   * @return The created {@link Crouton}.
   */
  public static Crouton makeText(Activity activity, int textResourceId, Style style, int viewGroupResId) {
    return makeText(activity, activity.getString(textResourceId), style,
      (ViewGroup) activity.findViewById(viewGroupResId));
  }


  /**
   * Creates a {@link Crouton} with provided text-resource and style for a given
   * activity.
   *
   * @param activity
   *   The {@link Activity} that the {@link Crouton} should be attached
   *   to.
   * @param customView
   *   The custom {@link View} to display
   *
   * @return The created {@link Crouton}.
   */
  public static Crouton make(Activity activity, View customView) {
    return new Crouton(activity, customView);
  }

  /**
   * Creates a {@link Crouton} with provided text-resource and style for a given
   * activity.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param customView
   *   The custom {@link View} to display
   * @param viewGroup
   *   The {@link ViewGroup} that this {@link Crouton} should be added to.
   *
   * @return The created {@link Crouton}.
   */
  public static Crouton make(Activity activity, View customView, ViewGroup viewGroup) {
    return new Crouton(activity, customView, viewGroup);
  }

  /**
   * Creates a {@link Crouton} with provided text-resource and style for a given
   * activity.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param customView
   *   The custom {@link View} to display
   * @param viewGroupResId
   *   The resource id of the {@link ViewGroup} that this {@link Crouton} should be added to.
   *
   * @return The created {@link Crouton}.
   */
  public static Crouton make(Activity activity, View customView, int viewGroupResId) {
    return new Crouton(activity, customView, (ViewGroup) activity.findViewById(viewGroupResId));
  }

  /**
   * Creates a {@link Crouton} with provided text and style for a given activity
   * and displays it directly.
   *
   * @param activity
   *   The {@link android.app.Activity} that the {@link Crouton} should
   *   be attached to.
   * @param text
   *   The text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   */
  public static void showText(Activity activity, CharSequence text, Style style) {
    makeText(activity, text, style).show();
  }

  /**
   * Creates a {@link Crouton} with provided text and style for a given activity
   * and displays it directly.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param text
   *   The text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   * @param viewGroup
   *   The {@link ViewGroup} that this {@link Crouton} should be added to.
   */
  public static void showText(Activity activity, CharSequence text, Style style, ViewGroup viewGroup) {
    makeText(activity, text, style, viewGroup).show();
  }

  /**
   * Creates a {@link Crouton} with provided text and style for a given activity
   * and displays it directly.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param text
   *   The text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   * @param viewGroupResId
   *   The resource id of the {@link ViewGroup} that this {@link Crouton} should be added to.
   */
  public static void showText(Activity activity, CharSequence text, Style style, int viewGroupResId) {
    makeText(activity, text, style, (ViewGroup) activity.findViewById(viewGroupResId)).show();
  }


  /**
   * Creates a {@link Crouton} with provided text and style for a given activity
   * and displays it directly.
   *
   * @param activity
   *   The {@link android.app.Activity} that the {@link Crouton} should
   *   be attached to.
   * @param customView
   *   The custom {@link View} to display
   */
  public static void show(Activity activity, View customView) {
    make(activity, customView).show();
  }

  /**
   * Creates a {@link Crouton} with provided text and style for a given activity
   * and displays it directly.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param customView
   *   The custom {@link View} to display
   * @param viewGroup
   *   The {@link ViewGroup} that this {@link Crouton} should be added to.
   */
  public static void show(Activity activity, View customView, ViewGroup viewGroup) {
    make(activity, customView, viewGroup).show();
  }

  /**
   * Creates a {@link Crouton} with provided text and style for a given activity
   * and displays it directly.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param customView
   *   The custom {@link View} to display
   * @param viewGroupResId
   *   The resource id of the {@link ViewGroup} that this {@link Crouton} should be added to.
   */
  public static void show(Activity activity, View customView, int viewGroupResId) {
    make(activity, customView, viewGroupResId).show();
  }

  /**
   * Creates a {@link Crouton} with provided text-resource and style for a given
   * activity and displays it directly.
   *
   * @param activity
   *   The {@link Activity} that the {@link Crouton} should be attached
   *   to.
   * @param textResourceId
   *   The resource id of the text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   */
  public static void showText(Activity activity, int textResourceId, Style style) {
    showText(activity, activity.getString(textResourceId), style);
  }

  /**
   * Creates a {@link Crouton} with provided text-resource and style for a given
   * activity and displays it directly.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param textResourceId
   *   The resource id of the text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   * @param viewGroup
   *   The {@link ViewGroup} that this {@link Crouton} should be added to.
   */
  public static void showText(Activity activity, int textResourceId, Style style, ViewGroup viewGroup) {
    showText(activity, activity.getString(textResourceId), style, viewGroup);
  }

  /**
   * Creates a {@link Crouton} with provided text-resource and style for a given
   * activity and displays it directly.
   *
   * @param activity
   *   The {@link Activity} that represents the context in which the Crouton should exist.
   * @param textResourceId
   *   The resource id of the text you want to display.
   * @param style
   *   The style that this {@link Crouton} should be created with.
   * @param viewGroupResId
   *   The resource id of the {@link ViewGroup} that this {@link Crouton} should be added to.
   */
  public static void showText(Activity activity, int textResourceId, Style style, int viewGroupResId) {
    showText(activity, activity.getString(textResourceId), style, viewGroupResId);
  }

  /**
   * Cancels all queued {@link Crouton}s. If there is a {@link Crouton}
   * displayed currently, it will be the last one displayed.
   */
  public static void cancelAllCroutons() {
    Manager.getInstance().clearCroutonQueue();
  }

  /**
   * Clears (and removes from {@link Activity}'s content view, if necessary) all
   * croutons for the provided activity
   *
   * @param activity
   *   - The {@link Activity} to clear the croutons for.
   */
  public static void clearCroutonsForActivity(Activity activity) {
    Manager.getInstance().clearCroutonsForActivity(activity);
  }

  /**
   * Cancels a {@link Crouton} immediately.
   */
  public void cancel() {
    Manager manager = Manager.getInstance();
    manager.removeCroutonImmediately(this);
  }

  /**
   * Displays the {@link Crouton}. If there's another {@link Crouton} visible at
   * the time, this {@link Crouton} will be displayed afterwards.
   */
  public void show() {
    Manager.getInstance().add(this);
  }

  public Animation getInAnimation() {
    if ((this.inAnimation == null) && (this.activity != null)) {
      if (getStyle().inAnimationResId > 0) {
        this.inAnimation = AnimationUtils.loadAnimation(getActivity(), getStyle().inAnimationResId);
      } else {
        this.inAnimation = DefaultAnimationsBuilder.buildDefaultSlideInDownAnimation();
      }
    }

    return inAnimation;
  }

  public Animation getOutAnimation() {
    if ((this.outAnimation == null) && (this.activity != null)) {
      if (getStyle().outAnimationResId > 0) {
        this.outAnimation = AnimationUtils.loadAnimation(getActivity(), getStyle().outAnimationResId);
      } else {
        this.outAnimation = DefaultAnimationsBuilder.buildDefaultSlideOutUpAnimation();
      }
    }

    return outAnimation;
  }

  /**
   * @param lifecycleCallback
   *   Callback object for notable events in the life of a Crouton.
   */
  public void setLifecycleCallback(LifecycleCallback lifecycleCallback) {
    this.lifecycleCallback = lifecycleCallback;
  }

  /**
   * @return <code>true</code> if the {@link Crouton} is being displayed, else
   *         <code>false</code>.
   */
  boolean isShowing() {
    return (activity != null) && (croutonView != null) && (croutonView.getParent() != null);
  }

  /**
   * Removes the activity reference this {@link Crouton} is holding
   */
  void detachActivity() {
    activity = null;
  }

  /**
   * Removes the viewGroup reference this {@link Crouton} is holding
   */
  void detachViewGroup() {
    viewGroup = null;
  }

  /**
   * Removes the lifecycleCallback reference this {@link Crouton} is holding
   */
  void detachLifecycleCallback() {
    lifecycleCallback = null;
  }

  /**
   * @return the lifecycleCallback
   */
  LifecycleCallback getLifecycleCallback() {
    return lifecycleCallback;
  }

  /**
   * @return the style
   */
  Style getStyle() {
    return style;
  }

  /**
   * @return the activity
   */
  Activity getActivity() {
    return activity;
  }

  /**
   * @return the viewGroup
   */
  ViewGroup getViewGroup() {
    return viewGroup;
  }

  /**
   * @return the text
   */
  CharSequence getText() {
    return text;
  }

  /**
   * @return the view
   */
  View getView() {
    // return the custom view if one exists
    if (this.customView != null) {
      return this.customView;
    }

    // if already setup return the view
    if (this.croutonView == null) {
      initializeCroutonView();
    }

    return croutonView;
  }

  private void initializeCroutonView() {
    Resources resources = this.activity.getResources();

    this.croutonView = initializeCroutonViewGroup(resources);

    // create content view
    RelativeLayout contentView = initializeContentView(resources);
    this.croutonView.addView(contentView);
  }

  private FrameLayout initializeCroutonViewGroup(Resources resources) {
    FrameLayout croutonView = new FrameLayout(this.activity);

    final int height;
    if (this.style.heightDimensionResId > 0) {
      height = resources.getDimensionPixelSize(this.style.heightDimensionResId);
    } else {
      height = this.style.heightInPixels;
    }

    final int width;
    if (this.style.widthDimensionResId > 0) {
      width = resources.getDimensionPixelSize(this.style.widthDimensionResId);
    } else {
      width = this.style.widthInPixels;
    }

    croutonView.setLayoutParams(
      new FrameLayout.LayoutParams(width != 0 ? width : FrameLayout.LayoutParams.MATCH_PARENT, height));

    // set background
    if (this.style.backgroundColorValue != -1) {
      croutonView.setBackgroundColor(this.style.backgroundColorValue);
    } else {
      croutonView.setBackgroundColor(resources.getColor(this.style.backgroundColorResourceId));
    }

    // set the background drawable if set. This will override the background
    // color.
    if (this.style.backgroundDrawableResourceId != 0) {
      Bitmap background = BitmapFactory.decodeResource(resources, this.style.backgroundDrawableResourceId);
      BitmapDrawable drawable = new BitmapDrawable(resources, background);
      if (this.style.isTileEnabled) {
        drawable.setTileModeXY(Shader.TileMode.REPEAT, Shader.TileMode.REPEAT);
      }
      croutonView.setBackgroundDrawable(drawable);
    }
    return croutonView;
  }

  private RelativeLayout initializeContentView(final Resources resources) {
    RelativeLayout contentView = new RelativeLayout(this.activity);
    contentView.setLayoutParams(new RelativeLayout.LayoutParams(RelativeLayout.LayoutParams.MATCH_PARENT,
      RelativeLayout.LayoutParams.WRAP_CONTENT));

    // set padding
    int padding = this.style.paddingInPixels;

    // if a padding dimension has been set, this will overwrite any padding
    // in pixels
    if (this.style.paddingDimensionResId > 0) {
      padding = resources.getDimensionPixelSize(this.style.paddingDimensionResId);
    }
    contentView.setPadding(padding, padding, padding, padding);

    // only setup image if one is requested
    ImageView image = null;
    if ((this.style.imageDrawable != null) || (this.style.imageResId != 0)) {
      image = initializeImageView();
      contentView.addView(image, image.getLayoutParams());
    }

    TextView text = initializeTextView(resources);

    RelativeLayout.LayoutParams textParams = new RelativeLayout.LayoutParams(RelativeLayout.LayoutParams.MATCH_PARENT,
      RelativeLayout.LayoutParams.WRAP_CONTENT);
    if (image != null) {
      textParams.addRule(RelativeLayout.RIGHT_OF, image.getId());
    }
    contentView.addView(text, textParams);
    return contentView;
  }

  private TextView initializeTextView(final Resources resources) {
    TextView text = new TextView(this.activity);
    text.setId(TEXT_ID);
    text.setText(this.text);
    text.setTypeface(Typeface.DEFAULT_BOLD);
    text.setGravity(this.style.gravity);
    
    // set the text color if set
    if (this.style.textColorResourceId != 0) {
      text.setTextColor(resources.getColor(this.style.textColorResourceId));
    }

    // Set the text size. If the user has set a text size and text
    // appearance, the text size in the text appearance
    // will override this.
    if (this.style.textSize != 0) {
      text.setTextSize(TypedValue.COMPLEX_UNIT_SP, this.style.textSize);
    }

    // Setup the shadow if requested
    if (this.style.textShadowColorResId != 0) {
      initializeTextViewShadow(resources, text);
    }

    // Set the text appearance
    if (this.style.textAppearanceResId != 0) {
      text.setTextAppearance(this.activity, this.style.textAppearanceResId);
    }
    return text;
  }

  private void initializeTextViewShadow(final Resources resources, final TextView text) {
    int textShadowColor = resources.getColor(this.style.textShadowColorResId);
    float textShadowRadius = this.style.textShadowRadius;
    float textShadowDx = this.style.textShadowDx;
    float textShadowDy = this.style.textShadowDy;
    text.setShadowLayer(textShadowRadius, textShadowDx, textShadowDy, textShadowColor);
  }

  private ImageView initializeImageView() {
    ImageView image;
    image = new ImageView(this.activity);
    image.setId(IMAGE_ID);
    image.setAdjustViewBounds(true);
    image.setScaleType(this.style.imageScaleType);

    // set the image drawable if not null
    if (this.style.imageDrawable != null) {
      image.setImageDrawable(this.style.imageDrawable);
    }

    // set the image resource if not 0. This will overwrite the drawable
    // if both are set
    if (this.style.imageResId != 0) {
      image.setImageResource(this.style.imageResId);
    }

    RelativeLayout.LayoutParams imageParams = new RelativeLayout.LayoutParams(
      RelativeLayout.LayoutParams.WRAP_CONTENT,
      RelativeLayout.LayoutParams.WRAP_CONTENT);
    imageParams.addRule(RelativeLayout.ALIGN_PARENT_LEFT, RelativeLayout.TRUE);
    imageParams.addRule(RelativeLayout.CENTER_VERTICAL, RelativeLayout.TRUE);
    return image;
  }

  @Override
  public String toString() {
    return "Crouton{" +
      "text=" + text +
      ", style=" + style +
      ", customView=" + customView +
      ", activity=" + activity +
      ", viewGroup=" + viewGroup +
      ", croutonView=" + croutonView +
      ", inAnimation=" + inAnimation +
      ", outAnimation=" + outAnimation +
      ", lifecycleCallback=" + lifecycleCallback +
      '}';
  }
}

```

## Error
Fix for crash when using an image in Crouton

## Error Description
Using Style.Builder to add an image (setImageResource() or .setImageDrawable() ) causes a crash when the Crouton is eventually inflated.

01-23 12:04:15.574: E/AndroidRuntime(4503): FATAL EXCEPTION: main
01-23 12:04:15.574: E/AndroidRuntime(4503): java.lang.NullPointerException
01-23 12:04:15.574: E/AndroidRuntime(4503):     at android.view.ViewGroup$LayoutParams.<init>(ViewGroup.java:5612)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at android.view.ViewGroup$MarginLayoutParams.<init>(ViewGroup.java:5838)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at android.widget.RelativeLayout$LayoutParams.<init>(RelativeLayout.java:1253)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at android.widget.RelativeLayout.generateLayoutParams(RelativeLayout.java:1013)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at android.view.ViewGroup.addViewInner(ViewGroup.java:3348)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at android.view.ViewGroup.addView(ViewGroup.java:3210)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at android.view.ViewGroup.addView(ViewGroup.java:3186)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at de.keyboardsurfer.android.widget.crouton.Crouton.initializeContentView(Crouton.java:682)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at de.keyboardsurfer.android.widget.crouton.Crouton.initializeCroutonView(Crouton.java:619)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at de.keyboardsurfer.android.widget.crouton.Crouton.getView(Crouton.java:607)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at de.keyboardsurfer.android.widget.crouton.Manager.addCroutonToView(Manager.java:191)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at de.keyboardsurfer.android.widget.crouton.Manager.handleMessage(Manager.java:160)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at android.os.Handler.dispatchMessage(Handler.java:99)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at android.os.Looper.loop(Looper.java:137)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at android.app.ActivityThread.main(ActivityThread.java:5039)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at java.lang.reflect.Method.invokeNative(Native Method)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at java.lang.reflect.Method.invoke(Method.java:511)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:793)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:560)
01-23 12:04:15.574: E/AndroidRuntime(4503):     at dalvik.system.NativeStart.main(Native Method)

Although, layout params are constructed for the resulting ImageView, it seems that they were not added to the ImageView !

Please find simple fix attached.

Cheers,
Damian

